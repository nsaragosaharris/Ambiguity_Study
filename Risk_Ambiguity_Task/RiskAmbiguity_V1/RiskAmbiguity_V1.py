#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on November 07, 2019, at 13:32
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'RiskAmbiguity_V1'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1536, 864), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "ChipsWelcomeScreen"
ChipsWelcomeScreenClock = core.Clock()
textwelcome_chips = visual.TextStim(win=win, name='textwelcome_chips',
    text="Welcome to the Chips Game.\n\nRemember to press '1' to choose the left option and '0' to choose the right option.\n\nWhen you are ready, press the spacebar to continue.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ISI_NoResponse"
ISI_NoResponseClock = core.Clock()
ISI_NoResponse_Fixation = visual.TextStim(win=win, name='ISI_NoResponse_Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Presentation_Trial"
Presentation_TrialClock = core.Clock()
trialimage = visual.ImageStim(
    win=win, name='trialimage',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.6,0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISI_fixation = visual.TextStim(win=win, name='ISI_fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ISI_NoResponse"
ISI_NoResponseClock = core.Clock()
ISI_NoResponse_Fixation = visual.TextStim(win=win, name='ISI_NoResponse_Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
endscreentext = visual.TextStim(win=win, name='endscreentext',
    text='End of experiment.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "ChipsWelcomeScreen"-------
t = 0
ChipsWelcomeScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
wait_for_spacebar_chips = event.BuilderKeyResponse()
# keep track of which components have finished
ChipsWelcomeScreenComponents = [textwelcome_chips, wait_for_spacebar_chips]
for thisComponent in ChipsWelcomeScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ChipsWelcomeScreen"-------
while continueRoutine:
    # get current time
    t = ChipsWelcomeScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textwelcome_chips* updates
    if t >= 0.0 and textwelcome_chips.status == NOT_STARTED:
        # keep track of start time/frame for later
        textwelcome_chips.tStart = t
        textwelcome_chips.frameNStart = frameN  # exact frame index
        textwelcome_chips.setAutoDraw(True)
    
    # *wait_for_spacebar_chips* updates
    if t >= 0.0 and wait_for_spacebar_chips.status == NOT_STARTED:
        # keep track of start time/frame for later
        wait_for_spacebar_chips.tStart = t
        wait_for_spacebar_chips.frameNStart = frameN  # exact frame index
        wait_for_spacebar_chips.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(wait_for_spacebar_chips.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if wait_for_spacebar_chips.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            wait_for_spacebar_chips.keys = theseKeys[-1]  # just the last key pressed
            wait_for_spacebar_chips.rt = wait_for_spacebar_chips.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ChipsWelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ChipsWelcomeScreen"-------
for thisComponent in ChipsWelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if wait_for_spacebar_chips.keys in ['', [], None]:  # No response was made
    wait_for_spacebar_chips.keys=None
thisExp.addData('wait_for_spacebar_chips.keys',wait_for_spacebar_chips.keys)
if wait_for_spacebar_chips.keys != None:  # we had a response
    thisExp.addData('wait_for_spacebar_chips.rt', wait_for_spacebar_chips.rt)
thisExp.nextEntry()
# the Routine "ChipsWelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ISI_NoResponse"-------
t = 0
ISI_NoResponseClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
ISI_NoResponseComponents = [ISI_NoResponse_Fixation]
for thisComponent in ISI_NoResponseComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ISI_NoResponse"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI_NoResponseClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI_NoResponse_Fixation* updates
    if t >= 0.0 and ISI_NoResponse_Fixation.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_NoResponse_Fixation.tStart = t
        ISI_NoResponse_Fixation.frameNStart = frameN  # exact frame index
        ISI_NoResponse_Fixation.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ISI_NoResponse_Fixation.status == STARTED and t >= frameRemains:
        ISI_NoResponse_Fixation.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI_NoResponseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI_NoResponse"-------
for thisComponent in ISI_NoResponseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
choicetrials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('RiskAmbiguity_ConditionFile_V1.xlsx'),
    seed=None, name='choicetrials')
thisExp.addLoop(choicetrials)  # add the loop to the experiment
thisChoicetrial = choicetrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisChoicetrial.rgb)
if thisChoicetrial != None:
    for paramName in thisChoicetrial.keys():
        exec(paramName + '= thisChoicetrial.' + paramName)

for thisChoicetrial in choicetrials:
    currentLoop = choicetrials
    # abbreviate parameter names if possible (e.g. rgb = thisChoicetrial.rgb)
    if thisChoicetrial != None:
        for paramName in thisChoicetrial.keys():
            exec(paramName + '= thisChoicetrial.' + paramName)
    
    # ------Prepare to start Routine "Presentation_Trial"-------
    t = 0
    Presentation_TrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    trialimage.setImage(ImageFile)
    right_or_left = event.BuilderKeyResponse()
    # keep track of which components have finished
    Presentation_TrialComponents = [trialimage, right_or_left]
    for thisComponent in Presentation_TrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Presentation_Trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Presentation_TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trialimage* updates
        if t >= 0.0 and trialimage.status == NOT_STARTED:
            # keep track of start time/frame for later
            trialimage.tStart = t
            trialimage.frameNStart = frameN  # exact frame index
            trialimage.setAutoDraw(True)
        frameRemains = 0.0 + 6.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if trialimage.status == STARTED and t >= frameRemains:
            trialimage.setAutoDraw(False)
        
        # *right_or_left* updates
        if t >= 0.0 and right_or_left.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_or_left.tStart = t
            right_or_left.frameNStart = frameN  # exact frame index
            right_or_left.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(right_or_left.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 6.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if right_or_left.status == STARTED and t >= frameRemains:
            right_or_left.status = STOPPED
        if right_or_left.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '0'])
            ResponseStartTime = t
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                right_or_left.keys = theseKeys[-1]  # just the last key pressed
                right_or_left.rt = right_or_left.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Presentation_TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    thisExp.addData('StimulusOnset', trialimage.tStart)
    thisExp.addData('ResponseStartTime', ResponseStartTime)
# -------Ending Routine "Presentation_Trial"-------
    for thisComponent in Presentation_TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if right_or_left.keys in ['', [], None]:  # No response was made
        right_or_left.keys=None
    choicetrials.addData('right_or_left.keys',right_or_left.keys)
    if right_or_left.keys != None:  # we had a response
        choicetrials.addData('right_or_left.rt', right_or_left.rt)
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [ISI_fixation]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI_fixation* updates
        if t >= 0.0 and ISI_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_fixation.tStart = t
            ISI_fixation.frameNStart = frameN  # exact frame index
            ISI_fixation.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ISI_fixation.status == STARTED and t >= frameRemains:
            ISI_fixation.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'choicetrials'


# ------Prepare to start Routine "ISI_NoResponse"-------
t = 0
ISI_NoResponseClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
ISI_NoResponseComponents = [ISI_NoResponse_Fixation]
for thisComponent in ISI_NoResponseComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ISI_NoResponse"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI_NoResponseClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI_NoResponse_Fixation* updates
    if t >= 0.0 and ISI_NoResponse_Fixation.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI_NoResponse_Fixation.tStart = t
        ISI_NoResponse_Fixation.frameNStart = frameN  # exact frame index
        ISI_NoResponse_Fixation.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ISI_NoResponse_Fixation.status == STARTED and t >= frameRemains:
        ISI_NoResponse_Fixation.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI_NoResponseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI_NoResponse"-------
for thisComponent in ISI_NoResponseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "EndScreen"-------
t = 0
EndScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [endscreentext]
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "EndScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endscreentext* updates
    if t >= 0.0 and endscreentext.status == NOT_STARTED:
        # keep track of start time/frame for later
        endscreentext.tStart = t
        endscreentext.frameNStart = frameN  # exact frame index
        endscreentext.setAutoDraw(True)
    frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
    if endscreentext.status == STARTED and t >= frameRemains:
        endscreentext.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
