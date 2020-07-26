# https://www.hackerrank.com/challenges/python-time-delta/problem

import datetime as dt

def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    
    d1 = dt.datetime.strptime(t1, format)
    d2 = dt.datetime.strptime(t2, format)
    
    diff = d1 - d2

    return str(int(abs(diff.total_seconds())))

if __name__ == "__main__":
    t1 = "Sun 10 May 2015 13:54:36 -0700"
    t2 = "Sun 10 May 2015 13:54:36 -0000"

    print(time_delta(t1, t2))

    t1 = "Sat 02 May 2015 19:54:36 +0530"
    t2 = "Fri 01 May 2015 13:54:36 -0000"
    print(time_delta(t1, t2))