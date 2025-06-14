def is_leapyear(year):
    if year % 400 == 0:
        leap_bool = True
    elif year % 100 == 0:
        leap_bool == False
    elif year % 4 == 0:
        leap_bool = True
    else:
        leap_bool = False

    return leap_bool

print(is_leapyear(input()))
