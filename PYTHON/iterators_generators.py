# ITERATION
'''Itération est l’une des fonctionnalités les plus fortes de Python. À un niveau élevé, vous pouvez simplement
 afficher itération comme un moyen de traiter les éléments dans une séquence. '''

items = [34, 67, 98]

'''Dans la plupart des cas, le statment for est utilisée pour une itération.'''
for it in items:
    print(it)

'''Cependant, de temps en temps, un problème exige un contrôle plus précis sur le mécanisme d’itération sous-jacent
anisme. Ainsi, il est utile de savoir ce qui se passe réellement.
L’exemple interactif suivant illustre la mécanique de base de ce qui se passe pendant l’itération '''

# Get the  iterator
it = iter(items) # invokes items.__iter__()
# Run the iterator
print(next(it)) # invokes it.__next__()
print(next(it))
print(next(it))


class Family:
    def __init__(self, value):
        self._value = value
        self._children = []
    
    def __str__(self):
        print(f'Node ({self._value})')

    def add_children(self, name):
        self._children.append(name)

    def __iter__(self):
        return iter(self._children)


ngampio = Family(7)
ngampio.add_children('Shider')
ngampio.add_children('Belghina')
for n in  ngampio: print(n)

it = iter(ngampio)
print(next(it))


#                        CREATE AN ITERATOR:
'''__iter__ : agit de la même façon, vous pouvez effectuer des opérations (initialisation etc.),
 mais vous devez toujours retourner l’objet itérateur lui-même.

__next__ : vous permet également de faire des opérations, 
 et doit retourner l’élément suivant dans la séquence.
 La méthode __next__ fait partie de __iter__ (return self).
'''

class Squares:
    def __init__(self, max):
        self.max = max
        self.n = 0
    def __iter__(self):
        return self #La méthode __next__ fait partie de __iter__
    def __next__(self):

        if self.n < self.max:
               self.n += 1
               return self.n ** 2 
        else:
                raise StopIteration

'''  OR if self.n == self.max:
            raise StopIteration
        self.n += 1
        return self.n ** 2'''
            
premier = Squares(5)
for i in premier: print(i)

first = Squares(3)
print(next(first))
print(next(first))


class Diplome:
    def __init__(self):
        self.diplomes = ['CEP', "BEPC", 'BAC', 'LICENCE', 'MASTER', 'DOCTORAT']
        self.i = 0
    def __getitem__(self,index):
        return self.diplomes[index]
    def __iter__(self):
        return self
    def __next__(self):
        for n in self.diplomes:
            if self.i < len(self.diplomes):
                self.i += 1
            else:
                raise StopIteration
            return f'Diplome number{self.i}: {n}'

sauvet = Diplome()
for i in sauvet: print(i)
    