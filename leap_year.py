def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 4) != 0:
        leap = False
    elif (year % 400) == 0:
        leap = True
    else:
        leap = False
    return leap

#year = int(input())

for i in range (1900,100000):
    print (i,is_leap(i))
