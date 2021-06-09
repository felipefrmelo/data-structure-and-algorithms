
from days_between_dates import Date, daysBetweenDates


def testMethodNextDayAndIncrementaDay():
    d1 = Date(2012, 11, 1)
    d2 = Date(2013, 12, 3)
    assert bool(d1 > d2) == False
    nextD = d1.nextDay()
    assert nextD.day == 2


def testMethodNextDayAndIncrementaMonth():
    d = Date(2012, 1, 31)
    nextD = d.nextDay()
    assert nextD.day == 1
    assert nextD.month == 2
    assert nextD.nextDay().day == 2
    assert nextD.nextDay().month == 2


def testMethodNextDayAndIncrementaAYear():
    d = Date(*(2012, 12, 31))
    nextD = d.nextDay()
    assert nextD.day == 1
    assert nextD.month == 1
    assert nextD.year == 2013


def testMethodGt():

    args = [((2012, 12, 30), (2012, 12, 30), False),
            ((2012, 12, 30), (2013, 1, 1), False),
            ((2013, 12, 30), (2012, 1, 1), True),
            ((2012, 12, 2), (2012, 1, 3), True),
            ((2012, 12, 30), (2012, 1, 31), True),
            ((2013, 1, 1), (2012, 1, 2), True),
            ((2012, 12, 30), (2012, 11, 30), True)]

    for d1, d2, want in args:
        assert bool(Date(*d1) > Date(*d2)) == want


def testIsALeepYear():
    d = Date(2012, 1, 1)
    assert d.isALeepYear


def testDaysBetweenDates():

    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((2000, 2, 1, 2000, 3, 1), 29),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        assert result == answer

