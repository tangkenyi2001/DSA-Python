class Robot:
    def __init__(self) -> None:
        self.age=1
    def getage(self):
        return self.age
    def setage(self,newage):
        self.age=newage
        

robot1=Robot()
robot1.setage(5)
print(robot1.getage())