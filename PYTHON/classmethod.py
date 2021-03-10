class Myclass:

    myclsattr = 5000

    @classmethod
    def myclassmethod(cls):
        cls.year = 2021
        return f'myclsattr = {cls.myclsattr} year = {cls.year}'

    def __init__(self):
        Myclass.year += 1
        Myclass.myclsattr += 1
        print(f'creat in {Myclass.year, Myclass.myclsattr}')

    

print(Myclass.myclassmethod())
print(Myclass.myclsattr)


p1 = Myclass()
print(p1.myclassmethod())

p2 = Myclass()

class Student:
    
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age # instance attribute

    @classmethod
    def getobject(cls):
        return cls('Steve', 25)

std1 = Student.getobject()
print(std1.age)
print(std1)
