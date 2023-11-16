class Auto:
    def __init__(self,brand,model,year,probeg):
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = probeg
    def getInfo(self):
        print(f'Марка:{self.brand}\nМодель:{self.model}\nДата выпуска:{self.year}\nПробег:{self.probeg}')
    def changeInfo(self,brand,model,year,probeg):
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = probeg

a = Auto('BMW','X6',2018,80000)
a.getInfo()
a.changeInfo('Merc','gl 203',2020,50000)
a.getInfo()
