int=[1,2,3,4]
print(int)
variety=[1,3,3.5]
print(variety)
newlist=variety
newlist.extend(int)#extend function
print(newlist)
newlist.pop()
print(newlist)

target=2
if target in newlist:
    print("In list")

def linear(list,target):
    for i,value in enumerate(list):
        #enumerate checks thes index and the value.
        if value==target:
            return i
    return -1

print(linear(newlist,3))
print(sum(newlist))
del int[0]
print(int)