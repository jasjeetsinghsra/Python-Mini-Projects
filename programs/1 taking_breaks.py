import time
import webbrowser

def taking_break(numberofbreaks,time_interval):
    i=0
    print "start time: ", time.ctime()
    while i<numberofbreaks:
        time.sleep(time_interval)
        webbrowser.open("https://www.youtube.com/watch?v=SQ1ED8-tBpE")
        i=i+1
    # no return statement required as the result need not be used in any other procedure etc.

taking_break(3,10)
