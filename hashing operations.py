from collections import deque
d = deque
d = deque([2,3,4,5])
print(d)
d.append(6) #inserts 6 at end of the queue
print(d)
d.appendleft(7) # appends at starting of the queue
print(d)
d.pop() # last added element will get deleted
print(d)
d.popleft() # removes the starting element
print(d)
d.extend([1,1]) #used to addd numbers at right
d.extendleft([0,9,8])#used to add numbers at left
print(d)
d.rotate(-3)##rotate by 3 to left
d.reverse()
print(d)
print(d.count(1))
d.insert(3,6) #inserts 6 at 4 th position
print(d)

######################################################
# import vectors
# v = vectors.vector([1,2,3])
# print(v+v)