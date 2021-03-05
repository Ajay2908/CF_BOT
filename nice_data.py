import datetime
import time


def lets_go(date_string):
    date = date_string[0:10]
    t = date_string[11:]
    year = int(date[0:4])
    month = int(date[5:7])
    daate = int(date[8:10])
    x = ''
    L = []
    for content in t:
        if(content != ':'):
            x += content
        else:
            L.append(int(x))
            x = ''

    a = year
    b = month
    c = daate
    d = L[0]
    e = L[1]
    dt = datetime.datetime(a, b, c, d, e)
    timestamp = time.mktime(dt.timetuple())
    timestamp += 19800
    return int(timestamp)



