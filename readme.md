timer
=====

A Python package to assist with measuring script running time.

### Sample usage
 
#### Stopwatch
    import time
    from timer.stopwatch import Stopwatch
    myStopwatch = Stopwatch()
    
    myStopwatch.start()
    time.sleep(2)
    myStopwatch.lap()
    time.sleep(3)
    myStopwatch.stop()
    
    print myStopwatch.summary
    Total time: 5.0
    Lap 1: 2.0
    Current Lap: 3.0
    

#### Timestamp
    from timer.timestamp import Timestamp
    theTime = Timestamp()
    
    print theTime.pretty()
    2013-04-01 11:45:58AM
    
    print theTime.raw()
    20130401114606