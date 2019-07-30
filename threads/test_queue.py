import queue

q = queue.Queue(100)
for i in range(100):
    myData = 'A'
    q.put(myData)
    myData = 'B'
while not q.empty():
    print(q.get())