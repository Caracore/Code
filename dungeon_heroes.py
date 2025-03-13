import random
version = "1.0.0"

class game():
    def __init__(self, gamemode, difficulty):
        self.gamemode = gamemode
        self.difficulty = difficulty
        if gamemode == "easy":
            self.difficulty = "easy"
        elif gamemode == "medium":
            self.difficulty = "medium"
        elif gamemode == "hard":
            self.difficulty = "hard"
        elif gamemode == "custom funny":
            self.difficulty = "custom funny" # menu_funny
        else:
            self.difficulty = "easy"

    class personnage():
        def __init__(self, nom, vie, attaque, defense, inventaire, argent):
            self.nom = nom
            self.vie = vie
            self.attaque = attaque
            self.defense = defense
            self.inventaire = inventaire
            self.argent = argent
            pass
        
        def __str__(self):
            return f"{self.nom} - {self.vie} - {self.attaque} - {self.defense} - {self.inventaire} - {self.argent}"
        
        def afficher_profile_personnage(self,):
            profile_player = self.__str__()
            print("Profile du personnage :\n" + profile_player, "\nInfo sur l'ennemi : ")

    class joueur(personnage):
        def __init__(self):
            super().__init__# rajouter input
            if self.gamemode == "easy" and self.difficulty == "easy":
                self.vie = 1000
                self.attaque = 100
                self.defense = 100
                self.inventaire = [] # rajouter items potions
            elif self.gamemode == "medium" and self.difficulty == "medium":
                self.vie = 500
                self.attaque = 50
                self.defense = 50
                self.inventaire = [] # rajouter items potions
            elif self.gamemode == "hard" and self.difficulty == "hard":
                self.vie = 500
                self.attaque = 25
                self.defense = 25
                self.inventaire = [] #NONE Potions
            elif self.gamemode == "custom funny" and self.difficulty == "custom funny":
                self.vie = 100
                self.attaque = 10
                self.defense = 10
                self.inventaire = [] #NONE Items after maj maybe custom items
        
        def __str__(self):
            return f"{self.nom} - {self.vie} - {self.attaque} - {self.defense} - {self.inventaire} - {self.argent}"
            pass
    
    class ally(personnage):
        def __init__(self):
            super().__init__# rajouter input
            pass
    
    class item():
        def __init__(self, nom, description, prix, vendeur, achat, vente, attaque, defense, power, type): # rajouter type
            self.nom = nom
            self.description = description
            self.prix = prix
            self.vendeur = vendeur
            self.achat = achat
            self.vente = vente
            self.attaque = attaque
            self.defense = defense
            self.power = power
            self.type = ["potion", "armure", "arme"]
            pass
    
    class potion(item):
        def __init__(self, nom, description, prix, vendeur, achat, vente, attaque, defense, power): # rajouter type
            super().__init__(nom, description, prix, vendeur, achat, vente, attaque, defense, power)
            pass
    
    class armure(item):
        def __init__(self, nom, description, prix, vendeur, achat, vente, attaque, defense, power): # rajouter type
            super().__init__(nom, description, prix, vendeur, achat, vente, attaque, defense, power)
            pass
    
    class arme(item):
        def __init__(self, nom, description, prix, vendeur, achat, vente, attaque, defense, power): # rajouter type
            super().__init__(nom, description, prix, vendeur, achat, vente, attaque, defense, power)
            pass
    
    class loot(item):
        def __init__(self, nom, description, prix, vendeur, achat, vente, attaque, defense, power, rareté, type): # rajouter type
            super().__init__(nom, description, prix, vendeur, achat, vente, attaque, defense, power, type)
            self.rareté = ["commun", "rare", "epique", "legendaire", "mythique", "insane"]
            pass

class ennemi():
    def __init__(self, nom, vie, attaque, defense, inventaire):
        self.nom = nom
        self.vie = vie
        self.attaque = attaque
        self.defense = defense
        self.inventaire = inventaire
        pass

class monstre(ennemi):
    def __init__(self, nom, vie, attaque, defense, inventaire):
        super().__init__(nom, vie, attaque, defense, inventaire)
        pass

class donjon():
    def __init__(self, nom, d_difficulty, d_loot, d_monstre, d_item):  # d_loot voir le loot potentiel
        self.nom = nom
        self.d_difficulty = d_difficulty
        self.d_loot = d_loot
        self.d_monstre = d_monstre
        self.d_item = d_item
        pass

class village():
    def __init__(self, nom, v_difficulty, v_loot, v_monstre, v_item):  # v_loot voir le loot potentiel
        self.nom = nom
        self.v_difficulty = v_difficulty
        self.v_loot = v_loot
        self.v_monstre = v_monstre
        self.v_item = v_item
        pass