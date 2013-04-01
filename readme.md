timer
=====

A Python package to assist with measuring script running time.

### Sample usage
 
    # stopwatch
    from timer import stopwatch
    myStopwatch = stopwatch.stopwatch()
    myStopwatch.start()
    myStopwatch.stop()
    myStopwatch.stop()
    

    # timestamps
    from timer import timestamp
    theTime = timestamp.timestamp()
    theTime.pretty()