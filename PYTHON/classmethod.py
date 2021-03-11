#      CLASS METHOD :
'''  - Le @classmethod décorateur est utilisé pour déclarer une class method
     - Le premier paramètre doit être cls, qui peut être utilisé pour accéder aux attributs de classe.
     - La class method ne peut accéder qu'aux class atttibutes (via cls) mais pas aux instance attrbutes.
     - Il peut renvoyer un objet de la classe.

  class methods peuvent modifier l'état de classe qui s'applique à toutes les instance objects
'''

# ACCES TO THE CLASS ATTRIBUTE:
class Prof:

    name = 'Unknow' #class attribute

    def __init__(self):
        self.age = 40 #instance attribute

    @classmethod
    def infos(cls):
        return f'prof name = {cls.name}'

'''class method n'ont pas besoin de instance object '''
print(Prof.infos())

'''Cependant, la même class méthod peut également être appelée en utilisant un instance object.'''
prof1 = Prof()
print(prof1.infos())



# CLASS METHOD TO GET AN OBJECT 
class Student:
    
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age # instance attribute

    @classmethod
    def getobject(cls):
        return cls('Steve', 25) # prend le meme nombre d'argument que dans __init__

std1 = Student.getobject()
print(std1.name)
print(std1.age)
print(std1)


class Myclass:

    myclsattr = 5000 #class attribute

    @classmethod
    def myclassmethod(cls):
        cls.year = 2021 # class method attribute 
        return f'myclsattr = {cls.myclsattr} year = {cls.year}'

    def __init__(self):
        Myclass.year += 1
        Myclass.myclsattr += 1
        print(f'creat in {Myclass.year, Myclass.myclsattr}')

    

print(Myclass.myclassmethod())
print(Myclass.myclsattr)
print(Myclass.year)


p1 = Myclass()
print(p1.myclassmethod())

p2 = Myclass()