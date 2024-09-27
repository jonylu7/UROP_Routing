class Vector:
    x=0
    y=0

    def __init__(self,x:float,y:float):
        self.x=x
        self.y=y

    def toListWithZ(self):
        return [self.x,self.y,0]

