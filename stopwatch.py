#!/usr/bin/env python
import time

class Stopwatch:

    __startTime__ = None
    __currentLap__ =  0
    laps = []
    summary = None
    state = 'Stopped'

    def __init__(self):        
        return
    
    def start(self):
        # Start the stopwatch.
        if not self.state == 'Stopped':
            print 'Stopwatch is already running.'
            return
        else:
            self.__startTime__ = time.time()
            self.state = 'Started'
        return
    
    def lap(self):
        # Start tracking a new lap.
        self.__update__()
        self.laps.append(self.__currentLap__)
        self.__currentLap__ = 0
        self.__startTime__ = time.time()
        self.__update__()
        return
        
    def stop(self):
        # Stop/Pause the stopwatch without clearing it.
        if self.state == 'Stopped':
            print 'Stopwatch isn\'t running.'
        else:
            self.__update__()
            self.state = 'Stopped'
        return
    
    def reset(self):
        # Reset the entire stopwatch back to zero.
        self.__startTime__ = None
        self.__currentLap__ = 0
        self.laps = []
        self.summary = None
        self.state = 'Stopped'
        return
        
    def __update__(self):
        # Internal function to update stopwatch summary.
        now = time.time()
            
        lapCounter = 1
        lapTime = 0
        lapSummary = ''
        for lap in self.laps:
            lapTime += lap
            lapSummary += '\nLap ' + str(lapCounter) + ': ' + str(lap)
            lapCounter += 1
            
        if not self.state == 'Stopped':
            self.__currentLap__ += (now - self.__startTime__)        
            
        totalTime = lapTime + self.__currentLap__
        self.summary = 'Total time: ' + str(totalTime) + lapSummary + '\nCurrent Lap: ' + str(self.__currentLap__)
        return
