class Voiture(object):

    def __init__(self, name, puissance):
        self._roues=4
        self.name = name
        self.puissance = puissance * self.roues


    def _get_roues(self):
        print ("Récupération du nombre de roues")
        return self._roues

    def _set_roues(self, v):
        print ("Changement du nombre de roues")
        self._roues  =  v

    roues=property(_get_roues, _set_roues)


limousine = Voiture('limousine', 100)
limousine.roues = 6
print(limousine.roues)
print(limousine.puissance)
limousine