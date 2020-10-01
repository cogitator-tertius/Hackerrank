def is_leap(year):
    leap = False
    # evenly divisible by 4, except 100 - but divisible by 400 counts
    # Write your logic here
    if year%4 == 0 and year%100 != 0:
        leap = True
    if year%400  == 00:
        leap = True
    return leap

year = int(input())
print(is_leap(year))