#         SPECIALS ATTRIBUTS
'''
 SPECIAL ATTRIBUTS in Python  start and end with the double underscores.
   Ils sont créés de manière implicite lors de la création d’une classe ou d'une fonction. 
   Ils contiennent des informations sur l'instance ou sur la fonction.
'''
# Class Special attributes
class  Telephone:
    '''fd'''
    date= 5
    def __init__(self 
        ):
        self.madein = 'china'
    def methodes1(
        self):
        return 'methode1 \
        '
    def methode2(self):
        w = Telephone.date + 1
        return w 

print(Telephone.__dict__)

samsung = Telephone()

print(samsung.__doc__) # Contient un commentaire associé à la classe
print(samsung.__module__) # Contient le nom du module dans lequel est incluse la classe	
print(samsung.__dict__)# Contient la liste des attributs de l’instance
print(samsung.__class__)# Contient le nom de la classe de l’instance. Ce nom est précédé du nom du module suivi d’un point.

# L’attribut __class__ contient lui même d’autres d’attributs :
print(samsung.__class__.__doc__) # Contient un commentaire associé à la classe 
print(samsung.__class__.__dict__) # Contient la liste des attributs de classe (statiques)
print(samsung.__class__.__name__) # Contient le nom de l’instance.
print(samsung.__class__.__bases__) # Contient les classes dont la classe de l’instance hérite
print(type(Telephone)
)

# Fonctions special attributes :