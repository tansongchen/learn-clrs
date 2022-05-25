from queue import PriorityQueue
l = []

p = PriorityQueue()
p.put(1)
p.put(2)
p.put(0)
print(p.get())
print(p.get())
print(2 in p)
