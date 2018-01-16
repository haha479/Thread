import threading
import time
from queue import Queue

#生产者
class Producer(threading.Thread):
	def run(self):
		global queue
		count = 0
		while True :
			#如果队列中的数据小于1000
			if queue.qsize() < 1000 :
				#生产100个产品
				for x in range(100):
					count += 1
					msg = "生产产品" + str(count)
					#将字符串加入到队列
					queue.put(msg)
					print(msg)
			time.sleep(0.5)
#消费者
class Consumer(threading.Thread):
	def run(self):
		global queue
		while True :
			#如果队列中的数据长度大于100
			if queue.qsize() > 100:
				for i in range(3):
					msg = self.name + "消费了" +queue.get()
					print(msg)
			time.sleep(1)
#创建队列
queue = Queue()

#初始队列中添加500个产品
for j in range(500):
	msgs = "初始产品" + str(j)
	queue.put(msgs)

#创建2个线程用于生产
for k in range(2):
	a1 = Producer()
	a1.start()

#创建5线程用于消费
for a in range(5):
	a2 = Consumer()
	a2.start()