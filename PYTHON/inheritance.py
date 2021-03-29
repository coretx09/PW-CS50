#decorator 


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
        self.words = 'we can'.split()
    def __add__(self, other):
        return Thirdclass(self.data + other) # makes a new instances 
    def __str__(self):
        return f"it's the Thirdclass {self.data}"
    def __mul__(self, other):
        self.data *= other
        return self.data
    def __getitem__(self,index):
        return self.words[index]

tc1 = Thirdclass(500)  # __init__ called
tc1.display() 
print(tc1) # __str__: returns display string
tc2 = tc1 + 5 * 2  # __add__: makes a new instance
print(tc1, tc2) #  zz has instance of Thirdclass
tc2.display() # zz has all ThirdClass methods
var1 = tc1 * 2 #  var1 = self.data of tc1
var2 = tc2 * 2  #  var2 = self.data of tc2 
print(var1, var2)
print(tc1, tc2, tc1[1])



# Customizing Constructors __init__:
class Person:
    def __init__(self, name, jobe=None, pay=0):
        self.name = name
        self.jobe =jobe
        self.pay = pay
    def __call__(self):
        return self.name, self.jobe, self.pay
# subclass
class Manager(Person):
    def __init__(self, name, pay): # Redefine constructor
        Person.__init__(self, name, 'manager', pay) # Run orignal with "mgr"

tom = Manager('TOM', pay=65000)
print(tom())

eric = Person('ERIC', 'programer', 150000)
print(eric())

# subclass
class Programer(Person):
    def __init__(self, name, pay):
        self.person = Person(name, 'programer', pay) #Embed a Person object



