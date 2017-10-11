#!/usr/bin/env python
from datetime import datetime, timedelta
from models.Models import db, Device
from app import create_app


class IEventCounter:

    def __init__(self):
        self.states = {
            "FSM1": 1,
            "FSM2": 2,
            "FSM3": 3,
            "FSM4": 4
        }

    # Summary
    #   Parse the event log to get it into a more easily parseable format
    # Param eventLog
    #   A file object pointing to a stream of lines representing time/value recordings
    # Returns
    #   A list of dictionaries [{timeInState, state}, ...]
    def _parseLog(self, eventLog):
        result = []
        previousTime = None
        previousState = None
        for line in eventLog:
            # split the input by tabs
            splitLine = line.rstrip('\r\n').split('\t')
            # get the time difference
            currentTime = datetime.strptime(splitLine[0]+" "+splitLine[1], "%Y-%m-%d %H:%M:%S")
            timeDiff = currentTime - previousTime if previousTime else timedelta(seconds=0)
            # get the current state
            currentState = int(splitLine[2])
            # append a dictionary with time difference and state
            result.append({
                "timeInState": timeDiff.seconds,
                "state": previousState
            });
            # advance the previous time
            previousTime = currentTime
            previousState = currentState
        result.append({
            "timeInState": 0,
            "state": previousState
        })
        return result


    # Summary
    #   Count faults in the parsedEventLog
    # Param parsedEventLog
    #   A list of dictionaries [{timeInState, state}, ...]
    # Returns
    #   Number of faults found in the parsed log file
    def _countParsedLog(self, parsedEventLog):
        # count the number of failures in the parsed log file
        # A failure is defined as:
        #   stage 3 for 5 minutes or more
        #   transition to stage 2
        #   any number of cycles between stages 2 and 3
        #   transition to 0 from either 2 or 3
        # This can be modeled as a finite state machine with 4 states (FSM1...FSM4)
        #   Start in FSM1
        #       3, >5min -> FSM2
        #       Anything else -> FSM1
        #   FSM2
        #       2 -> FSM3
        #       Anything else -> FSM1
        #   FSM3
        #       2,3 -> FSM3
        #       0 -> FSM4
        #       Anything else -> FSM1
        #   FSM4 (GOAL state)
        #       3, >5min -> FSM2
        #       Anything else -> FSM1
        currentFSMState = self.states["FSM1"]
        count = 0
        for event in parsedEventLog:
            state = event.get("state")
            timeInState = event.get("timeInState")
            if currentFSMState == self.states["FSM1"]:
                if state == 3 and timeInState >= 5*60:
                    currentFSMState = self.states["FSM2"]
            elif currentFSMState == self.states["FSM2"]:
                if (state == 2):
                    currentFSMState = self.states["FSM3"]
                else:
                    currentFSMState = self.states["FSM1"]
            elif currentFSMState == self.states["FSM3"]:
                if (state == 2 or state == 3):
                    currentFSMState = self.states["FSM3"]
                elif state == 0:
                    currentFSMState = self.states["FSM4"]
                else:
                    currentFSMState = self.states["FSM1"]
            if currentFSMState == self.states["FSM4"]:
                count += 1
                currentFSMState = self.states["FSM1"]
        return count;

    # Summary
    #   Parse and accumulate event information from the given log information
    # Param deviceID
    #   ID of the device that the log is associated with
    # Param eventLog
    #   A stream of lines representing time/value recordings
    def parseEvents(self, deviceId, eventLog):
        app = create_app()
        with app.app_context():
            device = Device.query.filter_by(deviceId=deviceId).first()
            if not device:
                device = Device(deviceId=deviceId, faultCount=0)
                db.session.add(device)
            currentCount = device.faultCount
            device.faultCount = currentCount + self._countParsedLog(self._parseLog(eventLog))
            db.session.commit()

    # Summary
    #   Gets the current count of events detected for the given deviceID
    # Param deviceID
    #   The device id of the device for which the fault count will be returned
    # Returns
    #   An integer representing the number of detected events
    def getEventCount(self, deviceId):
        app = create_app()
        with app.app_context():
            device = Device.query.filter_by(deviceId=deviceId).first()
            return device.faultCount if device else 0;
