#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on Thu Nov 14 15:58:38 2019
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'RiskAmbiguity_V1'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/nataliesaragosa-harris/Box/College_transition_study_(CTS)/Tasks/Lab Session/Chips/RiskAmbiguity_V1/RiskAmbiguity_V1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "ChipsWelcomeScreen"
ChipsWelcomeScreenClock = core.Clock()
textwelcome_chips = visual.TextStim(win=win, name='textwelcome_chips',
    text="Welcome to the Chips Game.\n\nRemember to press '1' to choose the left option and '0' to choose the right option.\n\nWhen you are ready, press the spacebar to continue.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
wait_for_spacebar_chips = keyboard.Keyboard()

# Initialize components for Routine "ISI_NoResponse"
ISI_NoResponseClock = core.Clock()
ISI_NoResponse_Fixation = visual.TextStim(win=win, name='ISI_NoResponse_Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Presentation_Trial"
Presentation_TrialClock = core.Clock()
trialimage = visual.ImageStim(
    win=win,
    name='trialimage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.6,0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
right_or_left = keyboard.Keyboard()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISI_fixation = visual.TextStim(win=win, name='ISI_fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI_NoResponse"
ISI_NoResponseClock = core.Clock()
ISI_NoResponse_Fixation = visual.TextStim(win=win, name='ISI_NoResponse_Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
endscreentext = visual.TextStim(win=win, name='endscreentext',
    text='End of experiment.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "ChipsWelcomeScreen"-------
# update component parameters for each repeat
wait_for_spacebar_chips.keys = []
wait_for_spacebar_chips.rt = []
# keep track of which components have finished
ChipsWelcomeScreenComponents = [textwelcome_chips, wait_for_spacebar_chips]
for thisComponent in ChipsWelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ChipsWelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ChipsWelcomeScreen"-------
while continueRoutine:
    # get current time
    t = ChipsWelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ChipsWelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textwelcome_chips* updates
    if textwelcome_chips.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textwelcome_chips.frameNStart = frameN  # exact frame index
        textwelcome_chips.tStart = t  # local t and not account for scr refresh
        textwelcome_chips.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textwelcome_chips, 'tStartRefresh')  # time at next scr refresh
        textwelcome_chips.setAutoDraw(True)
    
    # *wait_for_spacebar_chips* updates
    waitOnFlip = False
    if wait_for_spacebar_chips.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_for_spacebar_chips.frameNStart = frameN  # exact frame index
        wait_for_spacebar_chips.tStart = t  # local t and not account for scr refresh
        wait_for_spacebar_chips.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_for_spacebar_chips, 'tStartRefresh')  # time at next scr refresh
        wait_for_spacebar_chips.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(wait_for_spacebar_chips.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(wait_for_spacebar_chips.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if wait_for_spacebar_chips.status == STARTED and not waitOnFlip:
        theseKeys = wait_for_spacebar_chips.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            wait_for_spacebar_chips.keys = theseKeys.name  # just the last key pressed
            wait_for_spacebar_chips.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ChipsWelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ChipsWelcomeScreen"-------
for thisComponent in ChipsWelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textwelcome_chips.started', textwelcome_chips.tStartRefresh)
thisExp.addData('textwelcome_chips.stopped', textwelcome_chips.tStopRefresh)
# check responses
if wait_for_spacebar_chips.keys in ['', [], None]:  # No response was made
    wait_for_spacebar_chips.keys = None
thisExp.addData('wait_for_spacebar_chips.keys',wait_for_spacebar_chips.keys)
if wait_for_spacebar_chips.keys != None:  # we had a response
    thisExp.addData('wait_for_spacebar_chips.rt', wait_for_spacebar_chips.rt)
thisExp.addData('wait_for_spacebar_chips.started', wait_for_spacebar_chips.tStartRefresh)
thisExp.addData('wait_for_spacebar_chips.stopped', wait_for_spacebar_chips.tStopRefresh)
thisExp.nextEntry()
# the Routine "ChipsWelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ISI_NoResponse"-------
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
ISI_NoResponseComponents = [ISI_NoResponse_Fixation]
for thisComponent in ISI_NoResponseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI_NoResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ISI_NoResponse"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI_NoResponseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI_NoResponseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI_NoResponse_Fixation* updates
    if ISI_NoResponse_Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_NoResponse_Fixation.frameNStart = frameN  # exact frame index
        ISI_NoResponse_Fixation.tStart = t  # local t and not account for scr refresh
        ISI_NoResponse_Fixation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_NoResponse_Fixation, 'tStartRefresh')  # time at next scr refresh
        ISI_NoResponse_Fixation.setAutoDraw(True)
    if ISI_NoResponse_Fixation.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ISI_NoResponse_Fixation.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            ISI_NoResponse_Fixation.tStop = t  # not accounting for scr refresh
            ISI_NoResponse_Fixation.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISI_NoResponse_Fixation, 'tStopRefresh')  # time at next scr refresh
            ISI_NoResponse_Fixation.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI_NoResponseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI_NoResponse"-------
for thisComponent in ISI_NoResponseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_NoResponse_Fixation.started', ISI_NoResponse_Fixation.tStartRefresh)
thisExp.addData('ISI_NoResponse_Fixation.stopped', ISI_NoResponse_Fixation.tStopRefresh)

# set up handler to look after randomisation of conditions etc
choicetrials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('RiskAmbiguity_ConditionFile_V1.xlsx'),
    seed=None, name='choicetrials')
thisExp.addLoop(choicetrials)  # add the loop to the experiment
thisChoicetrial = choicetrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisChoicetrial.rgb)
if thisChoicetrial != None:
    for paramName in thisChoicetrial:
        exec('{} = thisChoicetrial[paramName]'.format(paramName))

for thisChoicetrial in choicetrials:
    currentLoop = choicetrials
    # abbreviate parameter names if possible (e.g. rgb = thisChoicetrial.rgb)
    if thisChoicetrial != None:
        for paramName in thisChoicetrial:
            exec('{} = thisChoicetrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Presentation_Trial"-------
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    trialimage.setImage(ImageFile)
    right_or_left.keys = []
    right_or_left.rt = []
    # keep track of which components have finished
    Presentation_TrialComponents = [trialimage, right_or_left]
    for thisComponent in Presentation_TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Presentation_TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Presentation_Trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Presentation_TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Presentation_TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trialimage* updates
        if trialimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialimage.frameNStart = frameN  # exact frame index
            trialimage.tStart = t  # local t and not account for scr refresh
            trialimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialimage, 'tStartRefresh')  # time at next scr refresh
            trialimage.setAutoDraw(True)
        if trialimage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trialimage.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                trialimage.tStop = t  # not accounting for scr refresh
                trialimage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trialimage, 'tStopRefresh')  # time at next scr refresh
                trialimage.setAutoDraw(False)
        
        # *right_or_left* updates
        waitOnFlip = False
        if right_or_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_or_left.frameNStart = frameN  # exact frame index
            right_or_left.tStart = t  # local t and not account for scr refresh
            right_or_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_or_left, 'tStartRefresh')  # time at next scr refresh
            right_or_left.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(right_or_left.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(right_or_left.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if right_or_left.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > right_or_left.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                right_or_left.tStop = t  # not accounting for scr refresh
                right_or_left.frameNStop = frameN  # exact frame index
                win.timeOnFlip(right_or_left, 'tStopRefresh')  # time at next scr refresh
                right_or_left.status = FINISHED
        if right_or_left.status == STARTED and not waitOnFlip:
            theseKeys = right_or_left.getKeys(keyList=['1', '0'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                right_or_left.keys = theseKeys.name  # just the last key pressed
                right_or_left.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Presentation_TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Presentation_Trial"-------
    for thisComponent in Presentation_TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    choicetrials.addData('trialimage.started', trialimage.tStartRefresh)
    choicetrials.addData('trialimage.stopped', trialimage.tStopRefresh)
    # check responses
    if right_or_left.keys in ['', [], None]:  # No response was made
        right_or_left.keys = None
    choicetrials.addData('right_or_left.keys',right_or_left.keys)
    if right_or_left.keys != None:  # we had a response
        choicetrials.addData('right_or_left.rt', right_or_left.rt)
    choicetrials.addData('right_or_left.started', right_or_left.tStartRefresh)
    choicetrials.addData('right_or_left.stopped', right_or_left.tStopRefresh)
    trialendtime = t
    thisExp.addData('TrialStartTime',trialimage.tStart)
    thisExp.addData('TrialEndTime',trialendtime)
    
    # ------Prepare to start Routine "ISI"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [ISI_fixation]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI_fixation* updates
        if ISI_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_fixation.frameNStart = frameN  # exact frame index
            ISI_fixation.tStart = t  # local t and not account for scr refresh
            ISI_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_fixation, 'tStartRefresh')  # time at next scr refresh
            ISI_fixation.setAutoDraw(True)
        if ISI_fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI_fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ISI_fixation.tStop = t  # not accounting for scr refresh
                ISI_fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ISI_fixation, 'tStopRefresh')  # time at next scr refresh
                ISI_fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    choicetrials.addData('ISI_fixation.started', ISI_fixation.tStartRefresh)
    choicetrials.addData('ISI_fixation.stopped', ISI_fixation.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'choicetrials'


# ------Prepare to start Routine "ISI_NoResponse"-------
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
ISI_NoResponseComponents = [ISI_NoResponse_Fixation]
for thisComponent in ISI_NoResponseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI_NoResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ISI_NoResponse"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI_NoResponseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI_NoResponseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI_NoResponse_Fixation* updates
    if ISI_NoResponse_Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI_NoResponse_Fixation.frameNStart = frameN  # exact frame index
        ISI_NoResponse_Fixation.tStart = t  # local t and not account for scr refresh
        ISI_NoResponse_Fixation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI_NoResponse_Fixation, 'tStartRefresh')  # time at next scr refresh
        ISI_NoResponse_Fixation.setAutoDraw(True)
    if ISI_NoResponse_Fixation.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ISI_NoResponse_Fixation.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            ISI_NoResponse_Fixation.tStop = t  # not accounting for scr refresh
            ISI_NoResponse_Fixation.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISI_NoResponse_Fixation, 'tStopRefresh')  # time at next scr refresh
            ISI_NoResponse_Fixation.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI_NoResponseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI_NoResponse"-------
for thisComponent in ISI_NoResponseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI_NoResponse_Fixation.started', ISI_NoResponse_Fixation.tStartRefresh)
thisExp.addData('ISI_NoResponse_Fixation.stopped', ISI_NoResponse_Fixation.tStopRefresh)

# ------Prepare to start Routine "EndScreen"-------
routineTimer.add(20.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [endscreentext]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "EndScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endscreentext* updates
    if endscreentext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endscreentext.frameNStart = frameN  # exact frame index
        endscreentext.tStart = t  # local t and not account for scr refresh
        endscreentext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endscreentext, 'tStartRefresh')  # time at next scr refresh
        endscreentext.setAutoDraw(True)
    if endscreentext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endscreentext.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            endscreentext.tStop = t  # not accounting for scr refresh
            endscreentext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(endscreentext, 'tStopRefresh')  # time at next scr refresh
            endscreentext.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endscreentext.started', endscreentext.tStartRefresh)
thisExp.addData('endscreentext.stopped', endscreentext.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
