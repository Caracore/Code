import personnage_init

class Joueur(personnage_init.Personnage):
    def __init__(self, nom, vie, force, defense):
        super().__init__(nom, vie, force, defense)
        self.inventaire = []
    
    def __str__(self):
        return f"{self.nom} (PV: {self.vie}/{self.max_vie}, Force: {self.force}, Défense: {self.defense})"
    #TODO: Voir quoi rajouter !

class PNJ(personnage_init.Personnage):
    def __init__(self, nom, vie, force, defense):
        super().__init__(nom, vie, force, defense)
    def donner_quest(self, quest):
        pass
    def donner_reward(self, reward):
        pass

    def __str__(self):
        return f"{self.nom} (PV: {self.vie}/{self.max_vie}, Force: {self.force}, Défense: {self.defense})"
    #TODO: Voir quoi rajouter !

class Ennemy(personnage_init.Personnage):
    def __init__(self, nom, vie, force, defense):
        super().__init__(nom, vie, force, defense)

    def __str__(self):
        return f"{self.nom} (PV: {self.vie}/{self.max_vie}, Force: {self.force}, Défense: {self.defense})"
    #TODO: Voir quoi rajouter !