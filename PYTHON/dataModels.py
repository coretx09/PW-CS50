#         SEQUENCES
# COLLECTIONS
import collections
from random import choice

# collections.namedtuple to construct a simple class to represent ---> individual cards
Card = collections.namedtuple('Card', ['rank', 'suit']) # Card: class
print(Card.__doc__)

beer_card = Card(4, 'moi')  # beer_card: class instance 
print(beer_card) 


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') # ranks list 
    suits = 'spades diamonds clubs hearts'.split() # scission des mots en list, suits list
    
    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.ranks
                                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __call__(self):
        return self._cards 

#     LIST RANKS & SUITS 
print(f'rank: {FrenchDeck.ranks} suit: {FrenchDeck.suits}')

#    INSTANCIATION
deck = FrenchDeck() 

#   MAGIC METHODS:
print(len(deck)) #called __len__
print(deck[50]) # called __getitem__
print(deck()) # called __call__

# collections
list1 = [str(x) for x in range(10, 16, 2)]
list2 = ['A', 'B', 'C']
Combine = collections.namedtuple('Combine',['nombre', 'mot'])
liste3 = [Combine(x, y) for x in list1 for y in list2]
print(liste3)

#Python already has a function to get a random item from a sequence: random.choice. 
print(choice(liste3))


# ELLIPSIS 
for card in deck:
    print(card)