#!/usr/bin/env python
import datetime

class Timestamp:
   
    def pretty(self):
        '''Return the current time in the format 2012-06-14 2:24:56pm.'''
        # Create a timestamp in the format yearmonthdayhoursminutesseconds'''
        theTime = datetime.datetime.now()
        timestamp = theTime.strftime("%Y-%m-%d %I:%M:%S%p")
        return timestamp
    
    def raw(self):
        '''Return the current time in the format 20120614142456.'''
        # Create a timestamp in the format yearmonthdayhoursminutesseconds'''
        theTime = datetime.datetime.now()
        timestamp = theTime.strftime("%Y%m%d%H%M%S")
        return timestamp
