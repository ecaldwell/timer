#!/usr/bin/env python
import datetime
import time
   
def pretty():
    '''Return the current time in the format 2012-06-14 2:24:56pm.'''
    theTime = datetime.datetime.now()
    timestamp = theTime.strftime("%Y-%m-%d %I:%M:%S%p")
    return timestamp

def raw():
    '''Return the current time in the format 20120614142456.'''
    theTime = datetime.datetime.now()
    timestamp = theTime.strftime("%Y%m%d%H%M%S")
    return timestamp

def unix():
    '''Return the current time in the format 1367770445.'''
    theTime time.time()
    return int(theTime)
