#             FONCTIONS (parametres.....)
""" Parametre(argument) est la variable répertoriée entre parenthèses dans la définition de fonction.
Par défaut, une fonction doit être appelée avec le nombre correct d'arguments.

 La définition de fonction n'exécute pas le corps de la fonction; ceci n'est exécuté que lorsque la fonction
  est appelée.

  Ils ont aussi des attributes speciales
"""

def maxlist(l:list):
    max = l[0]
    for i in l:
        if i > max:
            max = i
    print(f'le plus grand nombre = {max}')

liste = [87, 23, 34, 44,234]
maxlist(liste)

def minlist(l:list):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return f'le plus petit nombre = {min}'

print(minlist(liste))