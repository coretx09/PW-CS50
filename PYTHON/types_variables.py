#Variable
"""Ce terme désigne le fait d’attribuer un nom ou identificateur à des informations:
 en les nommant, on peut manipuler ces informations beaucoup plus facilement.

 Une variable est caractérisée par :
 -Un IDENTIFICATEUR : il peut contenir des lettres, des chiffres, des blancs soulignés
   mais il ne peut commencer par un chiffre.
 -Un TYPE : c’est une information sur le contenu de la variable qui indique à l’interpréteur
   python, la manière de manipuler cette information.
"""
x = 14
y = 45,0
z = True
name = 'sauvet007' 


#List
"""Les éléments de liste sont ordonnés, modifiables et autorisent
 les valeurs en double.
"""
names = ["Harry", "Ron", "Josh", "Mike"]
print(names[2])

names.append("Gims")
print(names)

#Set
""" Les éléments d'ensemble ne sont pas ordonnés, inchangeables
 et n'autorisent pas les valeurs en double.
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


#Dictionnary
"""Les éléments du dictionnaire ne sont pas ordonnés, modifiables
 et n'autorisent pas les doublons
  sont présentés dans des paires clé: valeur et peuvent être
  référencés à l'aide du nom de clé
"""
houses = {"Harry":  "nice", "Ron": "horrible"}