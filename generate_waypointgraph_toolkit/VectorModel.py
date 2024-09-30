class Vector:
    x=0
    y=0

    def __init__(self,x:float,y:float):
        self.x=x
        self.y=y

    def toListWithZ(self):
        return [self.x,self.y,0]

    def get(self,str:str):
        if(str=="x"):
            return self.x
        elif(str=="y"):
            return self.y

    def set(self,str:str,value:float):
        if(str=="x"):
            self.x=value
        elif(str=="y"):
            self.y=value

