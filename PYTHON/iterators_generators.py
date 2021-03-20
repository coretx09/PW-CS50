#     ITERATORS 
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