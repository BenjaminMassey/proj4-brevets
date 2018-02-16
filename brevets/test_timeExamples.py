# NOSE TESTS

import acp_times as a

def test_zero():
    # Distance of zero should hit an exception and just give an hour away
    assert a.open_time(0, 200, "2017-01-01T00:00") == "2017-01-01T00:00"
    assert a.close_time(0, 200, "2017-01-01T00:00") == "2017-01-01T01:00"
    assert a.open_time(0, 200, "2017-01-01T05:43") == "2017-01-01T05:43"
    assert a.close_time(0, 200, "2017-01-01T05:43") == "2017-01-01T06:43"

# Following 2 use this example from rusa.org/octime-acp.html calculator:
##400km ACP BREVET
##Checkpoint       Date  Time
##==========       ====  ====
##
##   40km    open: 01/01 01:11
##          close: 01/01 02:40
##
##   80km    open: 01/01 02:21
##          close: 01/01 05:20
##
##  150km    open: 01/01 04:25
##          close: 01/01 10:00
##
##  200km    open: 01/01 05:53
##          close: 01/01 13:20
def test_basicExampleOpens():
    start = "2017-01-01T00:00"
    assert a.open_time(40, 200, start) == "2017-01-01T01:11"
    assert a.open_time(80, 200, start) == "2017-01-01T02:21"
    assert a.open_time(150, 200, start) == "2017-01-01T04:25"
    assert a.open_time(200, 200, start) == "2017-01-01T05:53"
def test_basicExampleCloses():
    start = "2017-01-01T00:00"
    assert a.close_time(40, 200, start) == "2017-01-01T02:40"
    assert a.close_time(80, 200, start) == "2017-01-01T05:20"
    assert a.close_time(150, 200, start) == "2017-01-01T10:00"
    assert a.close_time(200, 200, start) == "2017-01-01T13:20"

def test_differentBrevets():
    # Different brevets with same start + distance should not change the times
    start = "2017-01-01T00:00"
    distance = 50
    assert a.open_time(distance, 90000, start) == a.open_time(distance, 2, start)
    assert a.close_time(distance, 3942, start) == a.close_time(distance, 0.2, start)

def test_handMath():
    # Here's an example from https://rusa.org/octime_alg.html that has the math written out
    start = "2017-01-01T00:00"
    control = 890
    brevet = 1000
    isoTimeDate = a.open_time(control, brevet, start)
    # They calculated total hours raw, so gonna need to convert
    isoDate = isoTimeDate.split("T")[0]
    isoTime = isoTimeDate.split("T")[1]
    days = int(isoDate.split("-")[2]) - 1 # - 1 since starting from day = 1
    hours = int(isoTime.split(":")[0])
    minutes = int(isoTime.split(":")[1])
    # Turn days and minutes into hours, add all together
    totalHours = (days * 24) + hours + (minutes / 60)
    # Compare our straight hours to their hand math
    comparison = totalHours / (200/34 + 200/32 + 200/30 + 290/28)
    # Make sure it's within a reasonable margin of error
    assert comparison > 0.97 and comparison < 1.03
