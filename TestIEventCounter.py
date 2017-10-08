#!/usr/bin/env python
import unittest
from IEventCounter import IEventCounter

class TestIEventCounter(unittest.TestCase):

    def testInput1(self):
        eventCounter = IEventCounter()
        f = open('./TestInputs/input1.csv', 'r')
        eventCounter.parseEvents("testDevice1", f)
        self.assertEqual(1, eventCounter.getEventCount("testDevice1"))

    def testInput2(self):
        eventCounter = IEventCounter()
        f = open('./TestInputs/input2.csv', 'r')
        eventCounter.parseEvents("testDevice2", f)
        self.assertEqual(2, eventCounter.getEventCount("testDevice2"))

    def testInput3(self):
        eventCounter = IEventCounter()
        f = open('./TestInputs/input3.csv', 'r')
        eventCounter.parseEvents("testDevice3", f)
        self.assertEqual(0, eventCounter.getEventCount("testDevice3"))

    def testInput4(self):
        eventCounter = IEventCounter()
        f = open('./TestInputs/input4.csv', 'r')
        eventCounter.parseEvents("testDevice4", f)
        self.assertEqual(1, eventCounter.getEventCount("testDevice4"))

if __name__ == '__main__':
    unittest.main()
