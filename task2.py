class Square:           #Прямоугольник,но как бы квадрат
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def S(self):
        return self.x*self.y
    def P(self):
        return (self.x+self.y)*2

s = Square(5,10)
print(s.S())
print(s.P())
