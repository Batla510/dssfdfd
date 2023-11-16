class Triangle:
    def __init__(self,a,b,c,h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def typeoftriangle(self):
        if self.a == self.b == self.c:
            print('Треугольник равносторонний')
        elif self.a == self.b or self.b == self.c or self.c == self.a:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')
    def S(self):
        s = self.a*self.h // 2
        print(s)
t = Triangle(4,4,4,4)
t.typeoftriangle()
t.S()

