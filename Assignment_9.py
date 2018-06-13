'''
#1
#import math
class circle:
    def __init__(self,r):
        self.r=r
    def getArea():
        return 3.14*self.r*self.r
    def getCircumference():
        return 2*.14*self.r
o=circle(5)
print(o.getArea())
'''
#2
class Student:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def display(self):
        print("Student's name:",self.name)
        print("Roll no. :",self.rno)
stu1 = Student("Vanshika",37)
stu1.display()

#3
class Temperature:
    def __init__(self,temp):
        self.temp=temp
    def convertFahrenheit(self):
        return self.temp*1.8+32
    def convertCelsius(self):
        return (self.temp-32)/1.8
t1=Temperature(32)
t1.convertCelsius()
t1.convertFahrenheit()

#4
class MovieDetails:
    def __init__(self,name, artistname,YOR,ratings):
        self.name=name
        self.artistname=artistname
        self.YOR=YOR
        self.ratings=ratings
    def display(self):
        print("Movie Name:",self.name)
        print("Artist:",self.artistname)
        print("Year of Release:",self.YOR)
        print("Ratings:",self.ratings)
    def update(self,name, artistname,YOR,ratings):
        self.name=name
        self.artistname=artistname
        self.YOR=YOR
        self.ratings=ratings
movie1=MovieDetails("3 Idiots","Aamir Khan",2013,4.5)
movie1.display()
movie1.update("Lagaan","Aamir Khan",2000,5)
movie1.display()
#5
class Expenditure:
    salary=0
    def __init__(self,exp,savings):
        self.exp=exp
        self.savings=savings
    def calculate(self):
        self.salary = self.exp+self.savings
    def dispExpSav(self):
        print("Total Expenditure:",self.exp)
        print("Total savings:",self.savings)
    def dispSal(self):
        print("Total Salary:",self.salary)
first=Expenditure(23000,7000)
first.calculate()
first.dispExpSav()
first.dispSal()
