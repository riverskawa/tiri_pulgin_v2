import time
import threading
import queue

# Worker 類別，負責處理資料
class Worker(threading.Thread):
  def __init__(self, queue, num):
    threading.Thread.__init__(self)
    self.queue = queue
    self.num = num

  def run(self):
    while self.queue.qsize() > 0:
      # 取得新的資料
      msg = self.queue.get()

      # 處理資料
      print("Worker %d: %s" % (self.num, msg))
      self.create_txt(msg)
    #   time.sleep(1)

  def create_txt(self,numsub):
    txt_name = './txt_folder/readme'+str(numsub)+'.txt'
    with open(txt_name, 'x') as f:
        f.write('Create a new text file!')


# 建立佇列
my_queue = queue.Queue()

# 將資料放入佇列
for i in range(158):
  my_queue.put("Data %d" % i)
    # my_queue.put(create_txt(i))

# 建立兩個 Worker
my_worker1 = Worker(my_queue, 1)
my_worker2 = Worker(my_queue, 2)
my_worker3 = Worker(my_queue, 3)
my_worker4 = Worker(my_queue, 4)
my_worker5 = Worker(my_queue, 5)
my_worker6 = Worker(my_queue, 6)
my_worker7 = Worker(my_queue, 7)
my_worker8 = Worker(my_queue, 8)
my_worker9 = Worker(my_queue, 9)
my_worker10 = Worker(my_queue, 10)
my_worker11 = Worker(my_queue, 11)
my_worker12 = Worker(my_queue, 12)
my_worker13 = Worker(my_queue, 13)
my_worker14 = Worker(my_queue, 14)
my_worker15 = Worker(my_queue, 15)
my_worker16 = Worker(my_queue, 16)
my_worker17 = Worker(my_queue, 17)
my_worker18 = Worker(my_queue, 18)
my_worker19 = Worker(my_queue, 19)
my_worker20 = Worker(my_queue, 20)

# 讓 Worker 開始處理資料
my_worker1.start()
my_worker2.start()
my_worker3.start()
my_worker4.start()
my_worker6.start()
my_worker7.start()
my_worker8.start()
my_worker9.start()
my_worker10.start()
my_worker11.start()
my_worker12.start()
my_worker13.start()
my_worker14.start()
my_worker15.start()
my_worker16.start()
my_worker17.start()
my_worker19.start()
my_worker20.start()


# 等待所有 Worker 結束
my_worker1.join()
my_worker2.join()
my_worker3.join()
my_worker4.join()
my_worker6.join()
my_worker7.join()
my_worker8.join()
my_worker9.join()
my_worker10.join()
my_worker11.join()
my_worker12.join()
my_worker13.join()
my_worker14.join()
my_worker15.join()
my_worker16.join()
my_worker17.join()
my_worker19.join()
my_worker20.join()

print("Done.")
