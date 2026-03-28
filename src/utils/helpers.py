"""General utility functions extracted from the SARS-CoV-2 evolution notebook."""
import time
import datetime
import numpy as np
import pandas as pd

def index_a(a, b, c):
    """Finds the index of the b-th occurrence of c in iterable a."""
    if b >= 0:
        init_num = 0
        for i, j in enumerate(a):
            if j == c:
                init_num += 1
                if init_num == b:
                    return i
    return -1

def dateadder(firstdate, days):
    """Returns a list of dates starting from firstdate for 'days' days."""
    alist = [firstdate]
    today = firstdate
    for _ in range(days - 1):
        dt = datetime.datetime.strptime(today, '%Y-%m-%d') + datetime.timedelta(days=1)
        today = dt.strftime('%Y-%m-%d')
        alist.append(today)
    return alist

def datefiller(firstdate, lastdate):
    """Fills dates between firstdate and lastdate inclusive."""
    start_dt = datetime.datetime.strptime(firstdate, '%Y-%m-%d')
    end_dt = datetime.datetime.strptime(lastdate, '%Y-%m-%d')
    if start_dt > end_dt:
        raise ValueError('The firstdate is later than the lastdate.')
    
    alist = []
    curr_dt = start_dt
    while curr_dt <= end_dt:
        alist.append(curr_dt.strftime('%Y-%m-%d'))
        curr_dt += datetime.timedelta(days=1)
    return alist

def middle_date(firstdate, lastdate):
    """Returns the middle date between two dates."""
    start_ts = time.mktime(time.strptime(firstdate, '%Y-%m-%d'))
    end_ts = time.mktime(time.strptime(lastdate, '%Y-%m-%d'))
    middle = int((start_ts + end_ts) / 2)
    return time.strftime('%Y-%m-%d', time.localtime(middle))

def compare(a, b):
    """Compares two strings (codons) and returns diff info."""
    diff = 0
    diffpos = []
    change = []
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            diff += 1
            diffpos.append(i)
            change.append(a[i] + '-' + b[i])
    if len(a) != len(b):
        diff += abs(len(a) - len(b))
    return {'diff': diff, 'diffpos': diffpos, 'change': change}

def dict_order(adict, Ascending=True):
    """Returns keys of dictionary sorted by their values."""
    import operator
    sorted_x = sorted(adict.items(), key=operator.itemgetter(1))
    final = [item[0] for item in sorted_x]
    if not Ascending:
        final = final[::-1]
    return final

def datetostamp(time_str):
    """
    Converts a date string to a timestamp.
    Fixed bug from original code: %Y-%M-%d (Minute) changed to %Y-%m-%d (Month).
    """
    return datetime.datetime.strptime(time_str, "%Y-%m-%d").timestamp()

def earlydate(date1, date2):
    """Returns True if date1 is strictly earlier than date2."""
    return datetostamp(date1) < datetostamp(date2)

def formtimeseq(adict):
    """Given an iterable of dates, returns them sorted chronologically."""
    tmp = []
    for what in adict:
        if len(what) == 10:
            if datetostamp(what) >= datetostamp('2019-10-22'):
                tmp.append(what)
    tmp.sort(key=datetostamp)
    return tmp

def indexs(lst):
    """Groups continuous numbers in a list into sublists."""
    indexlist = []
    from itertools import groupby
    fun = lambda x: x[1]-x[0]
    for k, g in groupby(enumerate(lst), fun):
        l1 = [j for i, j in g]
        indexlist.append(l1)
    return indexlist
