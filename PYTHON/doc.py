#  Explicit line joining: \
'''
 Deux lignes physiques ou plus peuvent être jointes en lignes logiques à l'aide de caractères de barre oblique
 inverse  
'''
if 10 < 65 or  \
    10 > 2: #Une ligne se terminant par une barre oblique inverse ne peut pas contenir de commentaire.'''
    print('yes')

mot = 'Merci\
 Sauvet'
print(mot)


#  Implicit line joining
'''Les expressions entre parenthèses, crochets ou accolades peuvent être divisées sur plusieurs lignes physiques 
sans utiliser de barres obliques inverse 
'''
untuple = (
    89,  # 89
    34, # Les lignes implicitement continues peuvent porter des commentaires. 
 '16'   #L'indentation des lignes de continuation n'est pas importante

  # Les lignes de continuation vierges sont autorisées
)
print(untuple)


#  Reserved classes of identifiers
'''
__*__   Dunder
__*   class private names
'''

# Escape Sequence (\)
phrase = "m'oi  je suis \\\\ //"
print(phrase)