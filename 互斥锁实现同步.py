import threading
import time

class H1(threading.Thread):
	def run(self):
		while True:
			mutex1.acquire()
			print("--H1执行--")
			time.sleep(1)
			mutex2.release()
class H2(threading.Thread):
	def run(self):
		while True:
			mutex2.acquire()
			print("--H2执行--")
			time.sleep(1)
			mutex3.release()
class H3(threading.Thread):
	def run(self):
		while True:
			mutex3.acquire()
			print("--H3执行--")
			time.sleep(1)
			mutex1.release()
#创建三把锁(2和3默认是锁上的)
mutex1 = threading.Lock()
mutex2 = threading.Lock()
mutex2.acquire()
mutex3 = threading.Lock()
mutex3.acquire()


h1 = H1()
h2 = H2()
h3 = H3()

h1.start()
h2.start()
h3.start()