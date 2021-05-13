#             FONCTIONS (parametres.....)
""" En termes simples, une Fonction est un dispositif qui regroupe un ensemble d’instructions afin qu’elles 
 puissent être exécutées plus d’une fois dans un programme.

Parametre(argument) est la variable répertoriée entre parenthèses dans la définition de fonction.
 Par défaut, une fonction doit être appelée avec le nombre correct d'arguments.

La définition de fonction n'exécute pas le corps de la fonction; ceci n'est exécuté que lorsque la fonction
  est appelée.

return statment peut apparaître n’importe où dans un corps de fonction ; lorsqu’elle est atteinte,
il termine l’appel de la fonction et renvoie un résultat à l’appelant.



  Ils ont aussi des attributes speciales
"""

def maxlist(l:list):
    max = l[0]
    for i in l:
        if i > max:
            max = i
    print(max)

liste = [87, 23, 34, 44,234]
a = maxlist(liste)
print(type(a), a)


def minlist(l:list):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min

b = minlist(liste)
print(type(b), b)


#      FACTORY FUNCTION:
