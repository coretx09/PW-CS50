#  A FIRST EXAMPLE
class Firstclass:  # define a class object 
    def setdata(self, value):
        self.data = value
        self._error = 'FUCK YOU'
    def display(self):
        print(f'{self.data} \n {self._error}')

x = Firstclass()
x.setdata(2500)
x.display()
x.data = 500 # can get/set attributes 
x.value = 6 # Can set new attributes here too!
print(x.value) # get attribute 


#          INHERITANCE 
#  A SECND EXAMPLE 
# SecondClass, that inherits all of FirstClass’s names and provides one of its own:

class Secondclass(Firstclass): # inherits setdata 
    def display(self):  # Changes display 
        print(f'Current value: {self.data}')

y = Secondclass()
y.setdata(56)  # Finds setdata in FirstClass
y.display() 


#        MAGIC METHODS
# A THIRD EXAMPLE
class Thirdclass(Secondclass):  # inherit from Secondclass
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return Thirdclass(self.data + other) # makes a new instances 
    def __str__(self):
        return f"it's the Thirdclass {self.data}"
    def __mul__(self, other):
        self.data *= other
        return self.data

z = Thirdclass(500)  # __init__ called
z.display() 
print(z) # __str__: returns display string
zz = z + 5 * 2  # __add__: makes a new instance
print(zz) #  zz has instance of Thirdclass
zz.display() # zz has all ThirdClass methods
k = z * 2 # 
kk = zz * 2
print(k)
print(zz)






