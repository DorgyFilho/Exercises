#160 - Há muito tempo

def Tempo():
    Year = int(input())
    while Year > 0:
        currentYear = int(input())
        if currentYear <= 2014:
            result = 2015 - currentYear
            print('%d D.C.' %result)
        else:
            result = currentYear - 2014
            print('%d A.C.' %result)
        Year -= 1

Tempo()