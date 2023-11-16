class Student:
    def __init__(self,name,surname,age,score):
        self.name = name
        self.surname = surname
        self.age = age
        self.score = score
    def getInfo(self):
        print(f'Имя:{self.name}\nФамилия:{self.surname}\nВозраст:{self.age}\nСр.балл:{self.score}')
    def changeInfo(self,name,surname,age,score):
        self.name = name
        self.surname = surname
        self.age = age
        self.score = score


a = Student('Vasya','Petrov',18,4.4)
a.getInfo()
a.changeInfo('BIBIBADSADDAS','FEFILOV',52,10.2)
a.getInfo()
