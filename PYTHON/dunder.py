#                       MAGIC OR DUNDER METHODS 
 
'''Magic methods in Python are the special methods that start and end with the double underscores.
 Les méthodes spéciales sont un ensemble de méthodes prédéfinies que vous pouvez utiliser
 pour enrichir vos classes, for example __init__ or __str__.

 Les méthodes magiques ne sont pas destinées à être invoquées directement par vous, 
 mais l'invocation se produit en interne depuis la classe sur une certaine action.
 Les méthodes Dunder vous permettent d'émuler le comportement des types intégrés.
 '''

# __str__ :
'''Lorsque vous print(miles), vous recevez un message d'apparence énigmatique, Ce message n'est pas très utile'''
class Dunder:
    pass
under = Dunder()
print(under)
'''Vous pouvez modifier ce qui est imprimé en définissant une méthode d'instance spéciale appelée .__str__().'''
class OtherDunder:
    def __str__(self):
        return 'la classe OtherDunder imprimer avec __str__'
other = OtherDunder()
print(other)


 




     
