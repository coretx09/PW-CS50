#Variable
"""Ce terme désigne le fait d’attribuer un nom ou identificateur à des informations:
 en les nommant, on peut manipuler ces informations beaucoup plus facilement.

    Variables are containers for storing data values.

 Une variable est caractérisée par :
 -Un IDENTIFICATEUR : il peut contenir des lettres, des chiffres, des blancs soulignés
   mais il ne peut commencer par un chiffre.
 -Un TYPE : c’est une information sur le contenu de la variable qui indique à l’interpréteur
   python, la manière de manipuler cette information.
"""
entier = 14
reel = 45,0
booleen = True
mot = 'sauvet007' 

#Variable immuable(immutable)
"""Une variable de type immuable ne peut être modifiée
 Une opération sur une variable de ce type entraîne nécessairement la création d’une 
 autre variable du même type qui intègrera la modification. 
 e.g: x += 1 ou x = x + 1 

 Les nombres, les chaînes de caractères,  et les tuple sont des types immutables

 Leurs contenus ne peuvent pas être modifié après sa création; ils peuvent donc être
 utilisé comme clé de dictionnaire ou comme élément d'un autre ensemble.
"""

#Variable modifiable(mutable)
"""Une variable de type modifiable peut être modifiée, elle conserve le même type et le même
 identificateur. C’est uniquement son contenu qui évolue.

 les listes et les dictionnaires sont modifiables
"""


#                               DATA MODEL


#ELLIPSIS types: Numbers(integer, booleans, float, complex)
'''This type has a single value. There is a single object with this value. 
This object is accessed through the literal ... or the built-in name Ellipsis. Its truth value is true.
'''

#TYPE DE SEQUENCES: string, list, tuple, range.
'''These represent finite ordered sets indexed by non-negative numbers. 
The built-in function len() returns the number of items of a sequence.
'''

  #List (MUTABLE)
"""Les éléments de liste sont ordonnés(INDEX), modifiables et autorisent
 les valeurs en double.
 Les listes sont créées à l'aide de crochets
 modifiable, ce qui signifie que nous pouvons modifier, ajouter et 
 supprimer des éléments dans une liste après sa création.
"""
names = ["Harry", "Ron", "Josh", "Mike"]
print(names[2])
names.append("Gims")
print(names)

  #Tuple (IMMUTABLE)
"""Les éléments de tuple sont ordonnés, inchangeables et autorisent les valeurs en double. 
 Un tuple apparaît comme une liste d’objets de tout type comprise entre parenthèses
 et séparés par des virgules.
"""
cordonnees = (34, 65, 105)
x = cordonnees[0]
y = cordonnees[1]
z = cordonnees[2]

x, y, z = cordonnees


#TYPE DE MAPPAGE:
#Dictionnary(MUTABLE)
"""Les éléments du dictionnaire ne sont pas ordonnés, modifiables
 et n'autorisent pas les doublons
  sont présentés dans des paires clé: valeur et peuvent être
  référencés à l'aide du nom de clé qui permet leur modification.
"""
houses = {"Harry":  "nice", "Ron": "horrible"}


#set TYPES
 #Set
""" Les éléments d'ensemble ne sont pas ordonnés, inchangeables (mais on peut ajouter les elmts)
 et n'autorisent pas les valeurs en double.

  Les utilisations courantes incluent le test d'appartenance, la suppression des doublons
  d'une séquence et le calcul d'opérations mathématiques telles que l'intersection,
  l'union, la différence et la différence symétrique.
"""
s = set()
# add elements to set
s.add(1)
s.add(2)
s.add(3)
print(s)

s.remove(2)
print(s)

ss = {34, True, True, 3.5, "34"}
print(ss)
print(len(ss))

# module 
'''On appele la fonction minlist() et maxlist() depuis le module test 
'''
from fonctions import maxlist

maliste = [45, 654, 87, 542, 0]
maxlist(maliste)


#CALLABLE types:
""" Voici les types auxquels l'opération d'appel de fonction peut etre applique 
     - Les fonctions définies par l'utilisateur (User-defined functions) ,
     - les fonctions intégrées (Built-in functions) e.g: len()......, 
     - Les méthodes des objets intégrés (Built-in methods), e.g: alist.append() [alist= list object, append()=Built-in methods ]
     - Class objects,
     - Instance methods
     - Et tous les objets ayant une __call__() méthode sont appelables.
       - Class instances arbitraires peuvent être rendues appelables en définissant une __call__()méthode dans leur classe.

 La définition de fonction n'exécute pas le corps de la fonction; ceci n'est exécuté que lorsque la fonction est appelée.
"""

 #User-defined functions (fonctions définies par l'utilisateur): 
"""Un objet fonction défini par l'utilisateur est créé par une définition de fonction(def fonctions(attributes).....)
  Ils ont aussi des attributes speciales"""

 #Instance methods
  
      
  