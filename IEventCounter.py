#!/usr/bin/env python

class IEventCounter:

    def __init__(self):
        self.deviceCounts = {}

    # Summary
    #   Parse the event log to get it into a more easily parseable format
    # Param eventLog
    #   A stream of lines representing time/value recordings
    # Returns
    #   A list of tuples [(a,b), (a,b)]
    def _parseLog(self, eventLog):
        result = []
        for line in eventLog:
            # get the time difference
            # get the state
            # construct and append a tuple to result
            result.append((line));
        print "parsed log:"
        print result
        return result



    def _countParsedLog(self, parsedEventLog):
        # count the number of failures in the parsed log file
        return 1;

    # Summary
    #   Parse and accumulate event information from the given log information
    # Param deviceID
    #   ID of the device that the log is associated with
    # Param eventLog
    #   A stream of lines representing time/value recordings
    def parseEvents(self, deviceID, eventLog):
        self.deviceCounts[deviceID] += self._countParsedLog(_parseLog(eventLog))
        print deviceID + " " + eventLog

    # Summary
    #   Gets the current count of events detected for the given deviceID
    # Param deviceID
    #   The device id of the device for which the fault count will be returned
    # Returns
    #   An integer representing the number of detected events
    def getEventCount(self, deviceID):
        return self.deviceCounts.get(deviceID) if self.deviceCounts.get(deviceID) else 0;
