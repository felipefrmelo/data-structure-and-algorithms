class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __eq__(self, other):
        return True if ((isinstance(other, self.__class__)
                         and (self.day, self.month, self.year) == (other.day, other.month, other.year))) else False

    def __lt__(self, other):
        return other > self

    def __gt__(self, other):
        if(self.year != other.year):
            return self.year > other.year
        if(self.month != other.month):
            return self.month > other.month

        if(self.day != other.day):
            return self.day > other.day

        return False

    def nextDay(self):
        if (self.day < self.getDaysInMonth()):
            return Date(self.year, self.month, self.day + 1)

        elif (self.month < 12):
            return Date(self.year, self.month + 1,  1)

        return Date(self.year + 1,  1,  1)

    def getDaysInMonth(self):
        if(self.month in (1, 3, 5, 7, 8, 10, 12)):
            return 31
        if (self.month in (4, 6, 9, 11)):
            return 30
        if(self.month == 2):
            return 29 if self.isALeepYear else 28

    @property
    def isALeepYear(self):
        if (self.year % 4 != 0):
            return False
        if (self.year % 100 != 0):
            return True

        return (self.year % 400 == 0)


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """

   
    d1 = Date(year1, month1, day1)
    d2 = Date(year2, month2, day2)
    days = 0
    while d1 < d2:
        d1 = d1.nextDay()
        days += 1
    return days
