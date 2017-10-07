#!/usr/bin/env python

class IEventCounter:

    def __init__(self):
        self.deviceCounts = {}

    # Summary
    #   Parse and accumulate event information from the given log information
    # Param deviceID
    #   ID of the device that the log is associated with
    # Param eventLog
    #   A stream of lines representing time/value recordings
    def parseEvents(deviceID, eventLog):
        print deviceID + " " + eventLog

    # Summary
    #   Gets the current count of events detected for the given deviceID
    # Param deviceID
    #   The device id of the device for which the fault count will be returned
    # Returns
    #   An integer representing the number of detected events
    def getEventCount(deviceID):
        return self.deviceCounts.get(deviceID)
