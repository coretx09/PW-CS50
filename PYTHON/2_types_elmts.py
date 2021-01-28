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
houses = {"Harry":  "Nice", "Ron": "horrible"}