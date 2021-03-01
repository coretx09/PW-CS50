class Vol:

    numero_vol = 0

    def __init__(self, destination, capacity):
        self.destination = destination
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




moscou_dubai = Vol('Dubai', 2)
moscou_dubai.add_passager('poups')
moscou_dubai.vol_infos()
moscou_dubai.add_passager('Kivi')
moscou_dubai.add_passager('zaika')
moscou_dubai.liste_passager('u')

dubai_moscou = Vol('Moscou', 5)
dubai_moscou.vol_infos()
dubai_moscou.add_passager('Galina')
del dubai_moscou.liste[0]
dubai_moscou.liste_passager('n')

print(moscou_dubai.__dict__)

