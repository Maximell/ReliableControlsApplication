#!/usr/bin/env python

import unittest
from IEventCounter import IEventCounter

class TestIEventCounter(unittest.TestCase):

    def testInput1(self):
        eventCounter = IEventCounter()
        f = open('./TestInputs/input1.csv', 'r')
        eventCounter.parseEvents("testDevice1", f)
        self.assertEqual(1, eventCounter.getEventCount("testDevice1"))

if __name__ == '__main__':
    unittest.main()
