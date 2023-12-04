from array import *
arr=array('i',[1,2,3,4,5])#i is for integer
for i in arr:
    print(i)
arr.insert(0,99)
arr.append(3)
print(arr)
arr.remove(1)
print(arr)
print(arr.pop())
arr.reverse()
print(arr)
print(arr.buffer_info())
