#node class
# a node consists of a value and the next node
#time complexity is o(1)
class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None
        
newnode=Node(5)
print(newnode)