p=dict(one='ein',two='zwei',three='drei')
dict1=p.copy()
print(p)

nedict=p.fromkeys([1,2,3],0)
print(nedict.get(1,"DNE"))# returns value of 1 key, else return dne
print(nedict.keys())
print(nedict.items())
print(nedict.setdefault(1,5))
print(nedict.pop(5,"none"))# pop the key 5, but if key 5 dne exist, return none which is the default value

newdict=dict(one='ein',two='zwei',three='drei')
newdict1=dict(four='ein',five='zwei',three='3')
newdict.update(newdict1)
print(newdict)
print("three" in newdict.keys())#check dict
print("three" in newdict.values())#check dict
#any if one key is true, output is true
#all if one key is true, output is false, need all keys to be true