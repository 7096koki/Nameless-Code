import calendar

def is_leap(year):
  if year < 0:
    leap_bool = False
  elif year == 0:
    leap_bool = True
  else:
    leap_bool = calendar.isleap(year)
  return leap_bool

test = int(input("閏年かどうか調べたい年を入力(例:2025):"))
print(is_leap(test))
