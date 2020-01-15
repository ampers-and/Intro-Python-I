"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

m_current = datetime.today().month
y_current = datetime.today().year


def print_cal(m=m_current, y=y_current):
    print(calendar.month(y, m))


# x = input("14_cal.py ").split(" ")
# y = [int(i) for i in x if i != '']

x = sys.argv
y = [int(i) for i in x if i != '14_cal.py']


if len(y) < 3:
    print_cal(*y)
else:
    print('Please enter the month and year in "mm yyyy" format')
