import numpy as np
twodarray=np.array([[0,0,0],[1,1,1],[2,2,2]])
#print(twodarray)
# axis 0 is row, axis 1 is column
newtwodarray=np.insert(twodarray,1,[3,3,3],axis=0)
print(newtwodarray)
newtwodarray=np.append(twodarray,[[3,3,3]],axis=0)
print(newtwodarray)
newtwodarray=np.append(twodarray,[[4],[4],[4]],axis=1)
print(newtwodarray)
print(len(newtwodarray))
newtwodarray=np.delete(twodarray,0,axis=1)
print(newtwodarray)
newtwodarray=np.delete(twodarray,0,axis=0)
print(newtwodarray)

def search(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
    #arr[0] will have same number of columns as arr[1]
            if array[i][j]==value:
                print(value)
search(newtwodarray,4)