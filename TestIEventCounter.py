#!/usr/bin/env python
import unittest
from IEventCounter import IEventCounter

class TestIEventCounter(unittest.TestCase):

    # Tests a minimal input file success
    def testInput1(self):
        eventCounter = IEventCounter()
        currentCount = eventCounter.getEventCount("testDevice1")
        f = open('./TestInputs/input1.csv', 'r')
        eventCounter.parseEvents("testDevice1", f)
        f.close()
        self.assertEqual(currentCount+1, eventCounter.getEventCount("testDevice1"))

    # Tests to ensure the algorithm can detect more than one fault in an input file
    def testInput2(self):
        eventCounter = IEventCounter()
        currentCount = eventCounter.getEventCount("testDevice2")
        f = open('./TestInputs/input2.csv', 'r')
        eventCounter.parseEvents("testDevice2", f)
        f.close()
        self.assertEqual(currentCount+2, eventCounter.getEventCount("testDevice2"))

    # Tests the 5 minute requirement (failure, 4:59 given)
    def testInput3(self):
        eventCounter = IEventCounter()
        currentCount = eventCounter.getEventCount("testDevice3")
        f = open('./TestInputs/input3.csv', 'r')
        eventCounter.parseEvents("testDevice3", f)
        f.close()
        self.assertEqual(currentCount+0, eventCounter.getEventCount("testDevice3"))

    # Tests the 5 minute requirement (success, 5:00 given)
    def testInput4(self):
        eventCounter = IEventCounter()
        currentCount = eventCounter.getEventCount("testDevice4")
        f = open('./TestInputs/input4.csv', 'r')
        eventCounter.parseEvents("testDevice4", f)
        f.close()
        self.assertEqual(currentCount+1, eventCounter.getEventCount("testDevice4"))

    # Test a failure followed by a success
    def testInput5(self):
        eventCounter = IEventCounter()
        currentCount = eventCounter.getEventCount("testDevice5")
        f = open('./TestInputs/input5.csv', 'r')
        eventCounter.parseEvents("testDevice5", f)
        f.close()
        self.assertEqual(currentCount+1, eventCounter.getEventCount("testDevice5"))

    # Test failure to move from FSM2->FSM3
    def testInput6(self):
        eventCounter = IEventCounter()
        currentCount = eventCounter.getEventCount("testDevice6")
        f = open('./TestInputs/input6.csv', 'r')
        eventCounter.parseEvents("testDevice6", f)
        f.close()
        self.assertEqual(currentCount+0, eventCounter.getEventCount("testDevice6"))

    # Test failure to move from FSM3->FSM4
    def testInput7(self):
        eventCounter = IEventCounter()
        currentCount = eventCounter.getEventCount("testDevice7")
        f = open('./TestInputs/input7.csv', 'r')
        eventCounter.parseEvents("testDevice7", f)
        f.close()
        self.assertEqual(currentCount+0, eventCounter.getEventCount("testDevice7"))

    # Test running multiple files for a single deviceID
    def testMultipleFileRuns(self):
        eventCounter = IEventCounter()
        currentCount = eventCounter.getEventCount("testDevice1")
        f = open('./TestInputs/input1.csv', 'r')
        eventCounter.parseEvents("testDevice1", f)
        f.close()
        f = open('./TestInputs/input2.csv', 'r')
        eventCounter.parseEvents("testDevice1", f)
        f.close()
        self.assertEqual(currentCount+3, eventCounter.getEventCount("testDevice1"))

    # Test running multiple files for multiple deviceID's
    def testMultipleFileRunsMultipleDevice(self):
        eventCounter = IEventCounter()
        currentCount1 = eventCounter.getEventCount("testDevice1")
        currentCount2 = eventCounter.getEventCount("testDevice2")
        f = open('./TestInputs/input1.csv', 'r')
        eventCounter.parseEvents("testDevice1", f)
        f.close()
        f = open('./TestInputs/input1.csv', 'r')
        eventCounter.parseEvents("testDevice1", f)
        f.close()
        f = open('./TestInputs/input2.csv', 'r')
        eventCounter.parseEvents("testDevice2", f)
        f.close()
        f = open('./TestInputs/input2.csv', 'r')
        eventCounter.parseEvents("testDevice2", f)
        f.close()
        self.assertEqual(currentCount1+2, eventCounter.getEventCount("testDevice1"))
        self.assertEqual(currentCount2+4, eventCounter.getEventCount("testDevice2"))

    # Test multiple transitions between stages 2 & 3 in input file
    def testInput8(self):
        eventCounter = IEventCounter()
        currentCount = eventCounter.getEventCount("testDevice8")
        f = open('./TestInputs/input8.csv', 'r')
        eventCounter.parseEvents("testDevice8", f)
        f.close()
        self.assertEqual(currentCount+1, eventCounter.getEventCount("testDevice8"))

    # Tests finding a pattern with excess before & after
    def testInput9(self):
        eventCounter = IEventCounter()
        currentCount = eventCounter.getEventCount("testDevice9")
        f = open('./TestInputs/input9.csv', 'r')
        eventCounter.parseEvents("testDevice9", f)
        f.close()
        self.assertEqual(currentCount+1, eventCounter.getEventCount("testDevice9"))

if __name__ == '__main__':
    unittest.main()
