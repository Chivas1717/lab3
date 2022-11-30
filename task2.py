import datetime


class Calendar:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, d):
        if not isinstance(d, int):
            raise TypeError("Wrong value of day")
        self.__day = d

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, m):
        if not isinstance(m, int):
            raise TypeError("Wrong value of month")
        self.__month = m

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if not isinstance(y, int):
            raise TypeError("Wrong value of year")
        self.__year = y

    def date(self):
        return datetime.datetime(self.__year, self.__month, self.__day)

    def __eq__(self, other):
        return self.date() == other.date()

    def __ne__(self, other):
        return self.date() != other.date()

    def __gt__(self, other):
        return self.date() > other.date()

    def __ge__(self, other):
        return self.date() >= other.date()

    def __lt__(self, other):
        return self.date() < other.date()

    def __le__(self, other):
        return self.date() <= other.date()

    def __iadd__(self, other):
        [d, m, y] = other
        if not isinstance(d, int):
            raise TypeError("Wrong value of day")
        if not isinstance(m, int):
            raise TypeError("Wrong value of month")
        if not isinstance(y, int):
            raise TypeError("Wrong value of year")

        if d + self.__day > 30:
            self.__day = (self.__day + d) - 30
            self.__month += 1
        else:
            self.__day += d
        if m + self.__month > 12:
            self.__month = (self.__month + d) - 12
            self.__year += 1
        else:
            self.__month += m

        self.__year += y
        return self

    def __isub__(self, other):
        [d, m, y] = other
        if not isinstance(d, int):
            raise TypeError("Wrong value of day")
        if not isinstance(m, int):
            raise TypeError("Wrong value of month")
        if not isinstance(y, int):
            raise TypeError("Wrong value of year")
        if d > self.__day:
            self.__day = 30 - (self.__day - d)
            self.__month -= 1
        if m > self.__month:
            self.__month = 12 - (self.__month - m)
            self.__month -= 1
        if y > self.__year:
            raise ValueError("Year < 0")

        self.__day -= d
        self.__month -= m
        self.__year -= y
        return self

    def __str__(self):
        return f'{self.__day}.{self.__month}.{self.__year}'


date1 = Calendar(17, 10, 2004)
date2 = Calendar(10, 3, 2021)
date1 += [16, 0, 16]
date2 -= [9, 2, 20]
print(date1)
print(date2 != date1)
print(date2 >= date1)

