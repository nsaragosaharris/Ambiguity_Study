import numpy as np
# import os
from nilearn.input_data import NiftiMasker
from nilearn import image
import pandas
import glob

'''
In the final csv, there should be a row for every actor. Each column should be the pair for the correlation.
Columns: Participant ID (same one just copied), Actor, AO_SUR_Corr, HO_SUR_Corr, HO_AO_Corr.
Rows: Each actor. So there should be 99 rows.
Then save each correlation in the correct column for that actor.
Here, I read in a template csv file that has these rows and columns but they are empty.
Could create within the script instead, but for ease I just have an empty one to use.
'''

# Function to mask data.
def setMasker(msk, smth):
    out = NiftiMasker(mask_img=msk, smoothing_fwhm=smth,
                      standardize=False, memory="nilearn_cache", memory_level=1)
    return (out)


# Template file has the list of all of the actors all of the participants should have seen.
# templatepath = '/u/home/n/nsaragos/scripts/cts/template_rsa_file.csv'
templatepath = '/Users/nataliesaragosa-harris/Desktop/cts/template_rsa_file.csv'
# studydir = '/u/project/silvers/data/CTS'
studydir = '/Users/nataliesaragosa-harris/Desktop/cts'
outputdir = '/Users/nataliesaragosa-harris/Desktop/cts/'

template = pandas.read_csv(templatepath, index_col="Actor")
# actors = template.index.values
# actors = ['HM10']
actors = ['HM10','AF08','HF10']
# participants = ['CTS001','CTS003','CTS004','CTS006','CTS009','CTS011','CTS012','CTS014','CTS019']
participants = ['CTS001']

'''
Loop 1: Go through every participant.
From their model folder, save the amygdala masks (in the same directory) for each run.
If there are not exactly three masks, print an error message.
should be run1_amy_bilat_Thr50.nii.gz, run2_amy_bilat_Thr50.nii.gz, and run3_amy_bilat_Thr50.nii.gz.
'''
for p in participants:
    print(p)
    pfile = template  # Start by using the empty template.
    pfile['Participant_ID'] = p  # Save participant ID (repeated) in the participant ID column.
    all_masks = glob.glob('%s/%s/model/run*_amy_bilat_Thr50.nii.gz' % (studydir, p))

    # The mask we are using here is the union of the three amygdala masks (one for each run),
    # specific to each participant. That is, it only includes voxels that were in all three run's amygdala masks.
    mask = glob.glob('%s/%s/model/allruns_amy_bilat_Thr50.nii.gz' % (studydir, p))

    # Using the file names, load the amygdala mask as an image.
    amy = image.load_img(mask)

    # It will give a warning because smoothing is set to 0, which is fine because we already smoothed
    # in the preprocessing stage.
    masker = setMasker(amy, 0)

    '''
    Loop 2: Go through every actor. Go to each run and find the actor (should be once per run).
    To do this, find the three .feat directory that match the actor name.
    (if there are not exactly three, print an error message).
    Search the name of the file to figure out which run (1, 2, or 3) and emotion type it is (AO, HO, or SUR).
    Remember, each actor should appear once per run (three times total), with a different emotion each type.
    '''
    for act in actors:  # go through every row (corresponds to an actor).
        # act = 'HF10'
        print(act)
        print('%s%s' % ('Loading actor: ', act))
        # There should be three trials (feat directories), all in different runs, that match this actor.
        trials = glob.glob('%s/%s/model/run*_lev1_lss-rsa_%s*.feat/stats/zstat1.nii.gz' % (studydir, p, act))

        if len(trials) != 3:  # Check that there are three trials.
            print("Error: This actor does not have three zstat trials.")
            continue

        # zstat1 should be the one to use for every trial.
        # I am looping through each run, which corresponds to each trial with that actor.
        allruns = ['run1', 'run2', 'run3']

        for run in allruns:
            print('%s%s' % ('Loading run: ', run))
            curr_trial = glob.glob('%s/%s/model/%s_lev1_lss-rsa_%s*.feat/stats/zstat1.nii.gz' % (studydir, p, run, act))
            print('%s%s' % ('Current image: ', curr_trial[0]))

            # Load in zstat image for each trial (within each run).
            curr_trial_img = image.load_img(curr_trial)

            # Using the masks created before with the masker function, transform the image to only
            # have the values within that mask. (check this function).

            curr_trial_z = masker.fit_transform(curr_trial_img)
            # Are these the voxel values? Should I save these in a file?

            # Now, we want to know what face type is in this trial.
            # curr_trial[0] to get the file name.
            # Then, save it to the correct one (surprised, angry, or happy).
            # run1_face[0].find("SUR")
            # If it contains the substring, will return the starting index. If not, returns -1.
            if curr_trial[0].find("SUR") != -1:
                SUR_face_z = curr_trial_z
            elif curr_trial[0].find("AO") != -1:
                AO_face_z = curr_trial_z
            elif curr_trial[0].find("HO") != -1:
                HO_face_z = curr_trial_z
            else:
                print("Error: Could not find any of the substrings.")
        # Now, for the current actor, there should be a surprised, angry, and happy face array (amygdala z values).
        AO_SUR_corr = np.corrcoef(SUR_face_z, AO_face_z)[0, 1]
        print(AO_SUR_corr)
        HO_SUR_corr = np.corrcoef(SUR_face_z, HO_face_z)[0, 1]
        print(HO_SUR_corr)
        AO_HO_corr = np.corrcoef(AO_face_z, HO_face_z)[0, 1]
        print(AO_HO_corr)
        # At this step, we want to save to pfile.
        # Find that actor's row, then add to correct column.
        # First check to make sure it doesn't equal None. If it does, print an error message.
        # If it does not, then add the value to the correct place.
        # index = (pfile[pfile['Actor'] == act]).index.values[0] # 35 for HF10 actor.
        # # assign correlations to correct column.
        # pfile["AO_SUR"][index] = AO_SUR_corr # gives warning.
        pfile.loc[act, "AO_SUR"] = AO_SUR_corr
        pfile.loc[act, "HO_SUR"] = HO_SUR_corr
        pfile.loc[act, "AO_HO"] = AO_HO_corr
        # update_values = pandas.DataFrame(data={"AO_SUR": [AO_SUR_corr], "HO_SUR": [HO_SUR_corr], "AO_HO": [AO_HO_corr]})
        # pfile[pfile.Actor == act].update(update_values)
        # Is there a way to make sure the SUR_face_z, etc. are empty at the end of the actor loop
        # so that it doesn't save the values from the previous actor?
        # SUR_AO_corr = None # can do this but seems weird because python is dynamic so i'm not sure.
    # Save pfile for the current participant.
    pfile.to_csv('%s%s_correlations.csv' % (outputdir, p))


################################################################################
# Code from https://dartbrains.org/features/notebooks/15_RSA.html
import os
import matplotlib.pyplot as plt
import seaborn as sns
from nltools.data import Brain_Data, Adjacency
from nltools.mask import expand_mask
from nltools.stats import fdr, threshold, fisher_r_to_z, one_sample_permutation
from sklearn.metrics import pairwise_distances
from nilearn.plotting import plot_glass_brain, plot_stat_map

# sub_list = [os.path.basename(x) for x in glob.glob(os.path.join(data_dir, 'S*'))]
# sub_list.sort()
# sub = sub_list[0]
#
# file_list = glob.glob(os.path.join(data_dir, sub, f'{sub}_beta*nii.gz'))
# file_list.sort()
# conditions = [os.path.basename(x)[:-7].split('_beta_')[-1] for x in file_list]
# beta = Brain_Data(file_list)

# Okay so I think for us, our file_list is the list of zstat1 images (correct? is this wrong? need to check).
file_list = glob.glob('%s/%s/model/run*_lev1_lss-rsa_%s*.feat/stats/zstat1.nii.gz' % (studydir, p, act))
beta = Brain_Data(file_list)

# Use apply_mask instead?
# https://nilearn.github.io/modules/generated/nilearn.masking.apply_mask.html#examples-using-nilearn-masking-apply-mask

# Load appropriate mask.
mask_file = glob.glob('%s/%s/model/allruns_amy_bilat_Thr50.nii.gz' % (studydir, p))
mask = Brain_Data(mask_file)
mask_exp = expand_mask(mask)
f = mask.plot()

out = []
for m in mask_exp:
    out.append(beta.apply_mask(m).distance(method='correlation'))