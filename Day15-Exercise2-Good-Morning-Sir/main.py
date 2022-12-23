#Learning to use modules in python
    #keywords:
    #module name time
    #time.ctime()
    #time.sleep(2) 2 is the parameter of sleep

import time #importing module time

seconds = time.time() #returns output in seconds
date = time.ctime(seconds) #converting the seconds into data using ctime inbuilt-keyword
print("Date : ",date)

time.sleep(2)
print("This is printed after 2s delay")