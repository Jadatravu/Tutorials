from datetime import datetime, timedelta

def main():
    """
       This is the solution for the problem 19
       https://projecteuler.net/problem=19
    """
    years_list = range(1901,2001)
    sundays_fm_year={}
    for y1 in years_list:
        d1 = datetime.strptime('Jan 1 %s'%str(y1), '%b %d %Y')
        td = timedelta(days=1)
        d2 = d1
        sundays_fm_year[y1] = 0
        for da in range(1,31):
            d2 = d2 + td 
            if d2.weekday() == 6:
               sundays_fm_year[y1] = sundays_fm_year[y1] + 1
        s1 = str(y1)+ str(" : ") +str(sundays_fm_year[y1])
        print s1

if __name__ == '__main__':
    main()
               

