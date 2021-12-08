queue  = [ "Jane", "Mark", "Dan"]
couple = ["Ann", "Max", "Pete"]


couple.reverse()
for i in range(len(couple)):
    queue.insert(0, couple[i])


for i in range(len(queue)):
    print(i, queue[i])

