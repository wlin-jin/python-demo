import time
from threading import Timer

def print_time(enter_time):
	print "now is " , time.time(), "your enter time is ", enter_time
	time.sleep(3)


print time.time()

Timer(5, print_time, (time.time(),)).start()
Timer(5, print_time, (time.time(),)).start()
print time.time()

