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

def print_cal():
  u_i = input("14_cal.py month [year]")
  elif len(u_i) <= 2 and u_i:
      print(calendar.TextCalendar(calendar.SUNDAY).formatmonth(2020, int(u_i)))
  elif len(u_i) > 2 and type(int(u_i[2:])) == int and type(int(u_i[0:2])) == int:
      print(calendar.TextCalendar(calendar.SUNDAY).formatmonth(int(u_i[2:]), int(u_i[0:2])))
  elif not u_i:
      print(calendar.TextCalendar(calendar.SUNDAY).formatmonth(2020, 1))
  elif type(int(u_i[2:])) != int or type(int(u_i[0:2])) != int:
      print('you must give a year and month to do this operation!')

print_cal()


