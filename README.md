# Project 4:  Brevet time calculator with Ajax

A reimplmentation of the calculator here:
https://rusa.org/octime_acp.html
based on the rules here:
https://rusa.org/octime_alg.html

Created by Benjamin Massey for CIS 322
(Based haveily on code given from the class)
Contact him at benjamin.w.massey@gmail.com

## Basics of the Calculations

All based around this table:

| Control Location (km) | Minimum Speed (km/hr) | Maximum Speed (km/hr) |
| --------------------- | --------------------- | --------------------- |
|        0 - 200        |          15           |          34           |
|       200 - 400       |          15           |          32           |
|       400 - 600       |          15           |          30           |
|       600 - 1000      |        11.428         |          28           |
|      1000 - 1300      |        13.333         |          26           |

It's actually rather simple. For opening time you use the maximum speed,
and for closing time you use the minimum speed. You just bracket up your
given time into these sections, convert using the time in the chart. For
parts of distances between 600 and 1000, use 28 for your open time, and
11.428 for your close time. Since you're going from distance to time, you
just divide your distance by the speed in the chart. The only real part
is the bracketing, where for a distance of 700, you would count it as 100
in the 600-1000 range, 200 in the 400-600 range, 200 in the 200-400 range,
and 200 in the 0-200 range.

All of this is done by the program, but there ya go!

## Weird Inputs

For the most part you can do whatever you want, but at the extremes it can
get a little weird. A distance of 0 is strange, and is defined on the
website to just give a set closing time of 1 hour. Times that are pretty
small or pretty large throw a note to the user, but should still work okay.

## Usage

The whole server is run from flask_brevets.py under the brevets folder. The
handling of user inputs is done in there and in the javascript under
calc.html in the templates directory. The calculations themselves are done
in acp_times.py. To make sure stuff is working, you can use nosetests in
the command line to run the tests in test_basicExamples.py.

# Have fun!