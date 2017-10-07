# ReliableControlsApplication
## Objective
Implement a processor that looks for and counts specific patterns in an event log.

## Problem Overview
A design flaw has been found in a type of HVAC unit. The unit can be in one of four stages (0-3)
depending on environmental conditions. The manufacturer has noted a design flaw where the unit can
accidentally go through a specific sequence of stages leading to possible damage.

The manufacturer has noted that a fault is indicated by four operations that occur in sequence:

  1. Stage 3 for five minutes or more
  2. Stage 2
  3. Any number of cycles between stage 2 and 3 for any duration
  4. Stage 0

Your task is to implement a log parser that detects and counts occurrences of this fault sequence.

Your parser should derive from the given IEventCounter interface and supply an implementation for two methods:
  1. void ParseEvents(string deviceID, StreamReader eventLog) - Inspect and parse a stream of operation records associated with a specific device, and count occurrrences of the "fault" sequence.
  2. int GetEventCount(string deviceId) - Gets the number of "fault" sequences observed for the given device.
  
## Log Format
Logs are in a tab separated CSV file with each row as a Time/Value pair.  Note that an entry is recorded each time the unit changes stage, however extra recordings may be taken (for a variety of reasons) that do not indicate a change of stage, and are simply redundant pieces of information.

For Example,

Timestamp		Value
2011-03-07 06:25:32	2
2011-03-07 09:15:55	3	← Indicates a stage change as previous recorded value is ‘2’
2011-03-07 12:00:00	3	← Redundant recording, possibly a “heartbeat”
2011-03-07 12:03:27	2	← Indicates a stage change
2011-03-07 20:23:01	0

Logs may contain any number of entries.  The end of a log is indicated by exhaustion of the Reader (i.e., no more data is available).

## Fault Event Pattern
Your implementation should count occurrences of a specific sequence of operation.  A fault occurs when a unit is in stage 3 for five minutes or more, followed by a direct transition to stage 2, followed by any number of cycles between stage 3 and 2, followed by a transition to stage 0 from either stage 2 or 3.

The following diagram illustrates the sequence of operations that lead to a fault:

Note: all log file entries can be assumed to be in chronological order.

## General Instructions
If you are unable to provide a complete solution, you should make every effort to provide a working submission – your code should compile without error and should supply at least some of the expected behavior.  We will evaluate your submission by applying a series of unit tests to verify that your implementation behaves as outlined in this specification.

In addition, we strongly encourage you to document your thoughts in comments, or a supplementary text file and include these notes as part of your submission.  This will allow us to evaluate the clarity of your thinking about the problem and solution approach.

We will also be evaluating the quality of the code you write and looking at the choices you make regarding naming, formatting, organization, decomposition, data structures, etc.

## Coding Instructions
The interface for constructing your solution in C# is provided, however you are welcome to code your solution in any main-stream, Object-Oriented programming language.  Regardless of what language you choose, your submission must:
  1. Implement the IEventCounter concept by supplying the two methods described above; and 
  2. Include testing to demonstrate your solution calculates the correct results under a variety of input conditions. 

## What to Submit
  1. Your implementation of the IEventCounter interface
  2. Any code you devised to test your implementation
  3. Any artifacts you feel are relevant (e.g., build instructions, notes on your approach, etc.)

## Bonus Challenge (not actually bonus): Basic MVC Website
Create a simple MVC website to display accumulated results.

A main index page should list all devices and their associated count values

The results should update dynamically on the client either every second, or every time the data changes. 



