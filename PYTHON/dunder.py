#                       MAGIC OR DUNDER METHODS 
 
'''Magic methods in Python are the special methods that start and end with the double underscores.
 Les méthodes spéciales sont un ensemble de méthodes prédéfinies que vous pouvez utiliser
 pour enrichir vos classes, for example __init__ or __str__.

 Les méthodes magiques ne sont pas destinées à être invoquées directement par vous, 
 mais l'invocation se produit en interne depuis la classe sur une certaine action.
 Les méthodes Dunder vous permettent d'émuler le comportement des types intégrés.
 '''

# Operator Overloading __str__ & __repr__
# __str__ :
'''Lorsque vous print(miles), vous recevez un message d'apparence énigmatique, Ce message n'est pas très utile'''
class Dunder:
    pass
under = Dunder()
print(under)
'''Vous pouvez modifier ce qui est imprimé en définissant une méthode d'instance spéciale appelée .__str__().'''
class OtherDunder:
    def __str__(self):
        return 'la classe OtherDunder imprimer avec __str__'
other = OtherDunder()
print(other)

   
class Operator:

    #CONSTRUCTOR:
    def __init__(self, value=89):
        self.data = value
        self.words = 'we can'.split()

    #OPERATOR + :    
    def __add__(self, other):
        return Operator(self.data + other) # makes a new instances 

    #PRINTING, CONVERSION print()    
    def __str__(self):
        return f"it's the Thirdclass {self.data}"

    #OPERATOR *:    
    def __mul__(self, other):
        self.data *= other
        return self.data

    #INDEXING, SLICING, ITERATION X[index], X[i:j], for loops and others iterations if no __iter__
    def __getitem__(self,index):
        return self.words[index]

    #INDEXING AND SLICE ASSIGNMENT X[index]=value, X[i:j]=iterable:
    def __setitem__(self, index, value):
        self.words[index] = value

    #LENGH:
    def __len__(self):
        return len(self.words)    

    #FUNCTION CALL:
    def __call__(self):
        print(self.words)

#   ___MAIN PROGRAM___ :

df = Operator()

#getitem:
print(df[1])
for i in df: print(i)
print('can' in df)

#len:
print(len(df))

#setitem:
df[1] = 'not'

#call
df()

#mul
df * 2

#------------------------0--------------------


# ITERATION 
class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop



     
