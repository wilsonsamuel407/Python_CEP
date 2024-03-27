# Take a year and a weekday as parameters, and then return the number of occurrences of a specific weekday in the year.

import calendar

class MyCalendar(calendar.Calendar):
    def __init__(self):
        super().__init__()

    def count_weekday_in_year(self,year,weekday):
        a = []
        for m in range(1,13):
            list = self.monthdays2calendar(year,m)
            for y in list:
                x = [l[1] for l in y if l[0] != 0]
                a += x
        print(a.count(weekday))
        

c = MyCalendar()
c.count_weekday_in_year(2000,6)



