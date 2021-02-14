class Vol:

    numero_vol = 0

    def __init__(self, destination, capacity):
        self.destination = destination
        self.capacity = capacity
        self.liste = []
        self.numero_passager = 0
        print(f'La capacite de notre vol est de {capacity} passagers a destination de {destination}' )
        Vol.numero_vol += 1
        

    def passager(self, name):
         if len(self.liste) < self.capacity  :
             self.liste.append(name)
             self.numero_passager += 1
             print(f'passager number {self.numero_passager} {name}')
         else:
             print(f'plus de place libre, sorry {name}')

        
    def liste_passager(self):
        print(f'Liste de passager:  {self.liste}')

    def vol_infos(self):
        print(f'Vole {Vol.numero_vol} infos:')
        print(f' Destination: {self.destination}')
        print(f' Capacite: {self.capacity}')
        print(f' Nombre de passager: {len(self.liste)}')
        print(f' Place libre: {self.capacity - len(self.liste)}')
        print(f' Liste passagers: {self.liste}')




'''

 vol1 = Vol('Dubai', 3)
vol1.passager('Sauvet')
vol1.passager('Galina')
vol1.passager('Koti')
vol1.liste_passager()

vol2 = Vol('Moscou', 2)
vol2.passager('Poups')
vol2.vol_infos()
vol2.passager('Kivi')
vol2.passager('Zaika')
 vol2.passager('Bebe')
'''

moscou_dubai = Vol('Dubai', 2)
moscou_dubai.passager('poups')
moscou_dubai.vol_infos()
moscou_dubai.passager('Kivi')
moscou_dubai.passager('zaika')