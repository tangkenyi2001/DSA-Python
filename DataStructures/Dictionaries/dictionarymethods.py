mydict=dict()
print(mydict)
mydict2={}
print(mydict2)
eng_sp=dict(one='ein',two='zwei',three='drei')
print(eng_sp)
eng_sp['one']='eins'
print(eng_sp)
eng_sp['four']='vier'
print(eng_sp)

def search(dict,letter):
    for i in dict:
        if dict[i]==letter:
            return i,letter
print(search(eng_sp,"zwei"))

del eng_sp['four']#key number
print(eng_sp)

#pop also returns the value on top of deleting it
removed=eng_sp.pop('four',None)
print(removed)
eng_sp.popitem()# removes the last element
print (eng_sp)
eng_sp.clear# clears the dict
