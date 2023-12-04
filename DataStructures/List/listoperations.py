a='spam'
b=list(a)
print(b)


a='spam spam spam'
delim='a'
b=a.split(delim)
print(b)
print(delim.join(b))

print(sorted(a))
print(a)