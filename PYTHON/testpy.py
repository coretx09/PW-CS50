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
    print(f'le plus petit nombre = {min}')

minlist(liste)
