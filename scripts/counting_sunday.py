# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# %%
import datetime as dt

def sunday_sums(start_date, end_date):
    sundays = 0
    date_ = start_date
    while date_ < end_date:
        if date_.isoweekday() == 7:
            sundays += 1

        if date_.month in [1,3,5,7,8,10,12]:
            days_ = 31
        elif date_.month == 2:
            if date_.year % 4 == 0 and str(date_.year)[-2:]!= "00":
                days_ = 29
            elif str(date_.year)[-2:] == "00" and  date_.year % 400:
                days_ = 29
            else:
                days_ = 28
        else:
            days_ = 30
        date_ += dt.timedelta(days=days_)

    return(sundays)
    

sunday_sums(dt.date(1901, 1, 1), dt.date(2001, 1, 1))
