prev_list=[1,2,3]
new_list=[]
for i in prev_list:
    new_list.append(i*2)
print (new_list)


new_list2=[item*3 for item in prev_list]
print (new_list2)


language="Python"
newlist3=[x for x in language]
print(newlist3)