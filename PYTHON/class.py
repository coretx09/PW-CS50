#   CLASS
""" Les classes fournissent un moyen de regrouper les données et les fonctionnalités.
             Les attributs sont les variables appartenant à une classe

 Class objects:
  Ils prennent en charge deux types d'opérations: attribute references and instantiation.
   -ATTRIBUTE REFERENCE:
      Ils utilisent la syntaxe standard utilisée pour toutes les références d'attributs en Python: obj.name [name=class attribut OR methods]
      Il existe deux types de name attributes valides: data attributes(instance variable) and methods

   -INSTANCITION:
     Class instantiation uses function notation, 
      instanceObject = Object(...)

 Instance objects:
  Les seules opérations comprises par les objets d'instance sont: attributes references (obj.name)

 
      
"""

class Vol: # class object = Vol

    numero_vol = 0 #class attribute(variable )

    def __init__(self, destination, capacity):  # Dunder or special method 
        self.destination = destination # instance attribute (variable)
        self.capacity = capacity
        self.liste = []
        self.numero_passager = 0
        print(5 * '------ -----')
        print(f'La capacite de notre vol est de {capacity} passagers a destination de {destination}' )
        Vol.numero_vol += 1
 
  # ADD NEW PASSAGER
    def add_passager(self, name):
         if len(self.liste) < self.capacity  :
             self.liste.append(name)
             self.numero_passager += 1
             print(f'CONGRATULATIONS {name.upper()} \n You are in fly to {self.destination}')
             print(f' passager number : {self.numero_passager} ({name})')
         else:
             print(f'plus de place libre, sorry {name}')
         print(3 * '---- ----')

  #LISTE DES PASSAGERS      
    def liste_passager(self, order):
        print('LISTE PASSAGERS:')
        if order.upper() == 'A':
            self.liste.sort()
        elif order.upper() == 'N':
            self.liste
        else:
            print('A - order alphabet \nB - order ticket')
        numero = 0
        for i in self.liste:
            numero += 1
            print(f'{numero}. passager {i[0].upper()}{i[1:]}') 
        print(3 * '---- ----')
 
  #FLY INFOS
    def vol_infos(self):
        print(f'FLY {Vol.numero_vol} INFOS:')
        print(f' Destination: {self.destination}')
        print(f' Capacite: {self.capacity}')
        print(f' Nombre de passager: {len(self.liste)}')
        print(f' Place libre: {self.capacity - len(self.liste)}')
        print(f' Liste passagers: {self.liste}')
        print(3 * '---- ----')




moscou_dubai = Vol('Dubai', 2) # instancation, instance object = moscou_dubai 
moscou_dubai.add_passager('poups') # attribute reference , name attribute: method 
moscou_dubai.vol_infos()
moscou_dubai.add_passager('Kivi')
moscou_dubai.add_passager('zaika')
moscou_dubai.liste_passager('u')

dubai_moscou = Vol('Moscou', 5) # instancation, instance object = dubai_moscou  
dubai_moscou.vol_infos()
dubai_moscou.add_passager('Galina')
del dubai_moscou.liste[0]
dubai_moscou.liste_passager('n')

print(moscou_dubai.__dict__) # attribute reference , name attribute: data attribute(special attribut)
print(moscou_dubai.__doc__)

print(Vol.numero_vol) # attribute reference, name attribute: data attribute(instance variable)