#PERSONNAGE INIT
class Personnage:
    """
    Classe représentant un personnage dans le jeu.
    """
    
    def __init__(self, nom, vie=100, force=10, defense=5):
        """
        Initialise un nouveau personnage.
        
        Args:
            nom (str): Le nom du personnage
            vie (int): Les points de vie du personnage
            force (int): La force du personnage
            defense (int): La défense du personnage
        """
        self.nom = nom
        self.vie = vie
        self.max_vie = vie
        self.force = force
        self.defense = defense
        self.inventaire = []
        
    def attaquer(self, cible):
        """
        Attaque une cible et lui inflige des dégâts.
        
        Args:
            cible (Personnage): Le personnage à attaquer
            
        Returns:
            int: Les dégâts infligés
        """
        degats = max(1, self.force - cible.defense)
        cible.subir_degats(degats)
        return degats
        
    def subir_degats(self, degats):
        """
        Fait subir des dégâts au personnage.
        
        Args:
            degats (int): Le montant de dégâts à subir
            
        Returns:
            bool: True si le personnage est toujours en vie, False sinon
        """
        self.vie = max(0, self.vie - degats)
        return self.vie > 0
        
    def soigner(self, montant):
        """
        Soigne le personnage d'un certain montant.
        
        Args:
            montant (int): Le montant de points de vie à restaurer
        """
        self.vie = min(self.max_vie, self.vie + montant)
        
    def ajouter_item(self, item):
        """
        Ajoute un item à l'inventaire du personnage.
        
        Args:
            item (Item): L'item à ajouter à l'inventaire
        """
        self.inventaire.append(item)
        
    def utiliser_item(self, index):
        """
        Utilise un item de l'inventaire.
        
        Args:
            index (int): L'index de l'item à utiliser
            
        Returns:
            bool: True si l'item a été utilisé avec succès, False sinon
        """
        if 0 <= index < len(self.inventaire):
            item = self.inventaire[index]
            if item.utiliser(self):
                if item.consommable:
                    self.inventaire.pop(index)
                return True
        return False
        
    def __str__(self):
        """
        Retourne une représentation textuelle du personnage.
        
        Returns:
            str: La représentation textuelle
        """
        return f"{self.nom} (PV: {self.vie}/{self.max_vie}, Force: {self.force}, Défense: {self.defense})"

#ITEM INIT
class Item:
    """
    Classe représentant un item dans le jeu.
    """
    
    def __init__(self, nom, description, consommable=True):
        """
        Initialise un nouvel item.
        
        Args:
            nom (str): Le nom de l'item
            description (str): La description de l'item
            consommable (bool): Indique si l'item disparaît après utilisation
        """
        self.nom = nom
        self.description = description
        self.consommable = consommable
        
    def utiliser(self, personnage):
        """
        Utilise l'item sur un personnage.
        Cette méthode doit être surchargée par les classes filles.
        
        Args:
            personnage: Le personnage qui utilise l'item
            
        Returns:
            bool: True si l'item a été utilisé avec succès, False sinon
        """
        # Méthode de base qui ne fait rien
        # À surcharger dans les classes dérivées
        return False
        
    def __str__(self):
        """
        Retourne une représentation textuelle de l'item.
        
        Returns:
            str: La représentation textuelle
        """
        return f"{self.nom}: {self.description}"


class PotionSoin(Item):
    """
    Classe représentant une potion de soin.
    """
    
    def __init__(self, nom="Potion de soin", description="Restaure des points de vie", puissance=20):
        """
        Initialise une nouvelle potion de soin.
        
        Args:
            nom (str): Le nom de la potion
            description (str): La description de la potion
            puissance (int): Le nombre de points de vie restaurés
        """
        super().__init__(nom, description, True)
        self.puissance = puissance
        
    def utiliser(self, personnage):
        """
        Utilise la potion pour soigner un personnage.
        
        Args:
            personnage: Le personnage qui utilise la potion
            
        Returns:
            bool: True si la potion a été utilisée avec succès
        """
        personnage.soigner(self.puissance)
        return True


class Arme(Item):
    """
    Classe représentant une arme.
    """
    
    def __init__(self, nom, description, bonus_force):
        """
        Initialise une nouvelle arme.
        
        Args:
            nom (str): Le nom de l'arme
            description (str): La description de l'arme
            bonus_force (int): Le bonus de force conféré par l'arme
        """
        super().__init__(nom, description, False)
        self.bonus_force = bonus_force
        
    def utiliser(self, personnage):
        """
        Équipe l'arme sur un personnage.
        
        Args:
            personnage: Le personnage qui utilise l'arme
            
        Returns:
            bool: True si l'arme a été équipée avec succès
        """
        # Logique pour équiper l'arme
        # Ici on pourrait ajouter le bonus de force au personnage
        return True


class Armure(Item):
    """
    Classe représentant une armure.
    """
    
    def __init__(self, nom, description, bonus_defense):
        """
        Initialise une nouvelle armure.
        
        Args:
            nom (str): Le nom de l'armure
            description (str): La description de l'armure
            bonus_defense (int): Le bonus de défense conféré par l'armure
        """
        super().__init__(nom, description, False)
        self.bonus_defense = bonus_defense
        
    def utiliser(self, personnage):
        """
        Équipe l'armure sur un personnage.
        
        Args:
            personnage: Le personnage qui utilise l'armure
            
        Returns:
            bool: True si l'armure a été équipée avec succès
        """
        # Logique pour équiper l'armure
        # Ici on pourrait ajouter le bonus de défense au personnage
        return True

#QUEST INIT
class Quest:
    """
    Classe représentant une quête dans le jeu.
    """
    
    def __init__(self, titre, description, objectif, recompense=None):
        """
        Initialise une nouvelle quête.
        
        Args:
            titre (str): Le titre de la quête
            description (str): La description détaillée de la quête
            objectif (str): L'objectif à accomplir
            recompense (Item, optional): La récompense obtenue à la fin de la quête
        """
        self.titre = titre
        self.description = description
        self.objectif = objectif
        self.recompense = recompense
        self.complete = False
    
    def completer(self):
        """
        Marque la quête comme complétée.
        
        Returns:
            Item: La récompense de la quête, si elle existe
        """
        self.complete = True
        return self.recompense
    
    def est_complete(self):
        """
        Vérifie si la quête est complétée.
        
        Returns:
            bool: True si la quête est complétée, False sinon
        """
        return self.complete
    
    def __str__(self):
        """
        Retourne une représentation textuelle de la quête.
        
        Returns:
            str: La représentation textuelle
        """
        status = "Complétée" if self.complete else "En cours"
        return f"{self.titre} ({status})\n{self.description}\nObjectif: {self.objectif}"

#WORLD INIT
class World:
    """
    Classe représentant le monde du jeu.
    """
    
    def __init__(self, nom, largeur, hauteur):
        """
        Initialise un nouveau monde.
        
        Args:
            nom (str): Le nom du monde
            largeur (int): La largeur de la carte du monde
            hauteur (int): La hauteur de la carte du monde
        """
        self.nom = nom
        self.largeur = largeur
        self.hauteur = hauteur
        self.carte = [[None for _ in range(largeur)] for _ in range(hauteur)]
        self.rooms = []
    
    def ajouter_room(self, room, x, y):
        """
        Ajoute une salle au monde à une position spécifique.
        
        Args:
            room (Room): La salle à ajouter
            x (int): La position x sur la carte
            y (int): La position y sur la carte
            
        Returns:
            bool: True si la salle a été ajoutée avec succès, False sinon
        """
        if 0 <= x < self.largeur and 0 <= y < self.hauteur:
            if x + room.largeur <= self.largeur and y + room.hauteur <= self.hauteur:
                # Vérifier que l'espace est libre
                for i in range(y, y + room.hauteur):
                    for j in range(x, x + room.largeur):
                        if self.carte[i][j] is not None:
                            return False
                
                # Placer la salle sur la carte
                for i in range(y, y + room.hauteur):
                    for j in range(x, x + room.largeur):
                        self.carte[i][j] = room
                
                room.position = (x, y)
                self.rooms.append(room)
                return True
        return False
    
    def obtenir_room(self, x, y):
        """
        Obtient la salle à une position spécifique.
        
        Args:
            x (int): La position x sur la carte
            y (int): La position y sur la carte
            
        Returns:
            Room: La salle à la position spécifiée, ou None si aucune salle n'est présente
        """
        if 0 <= x < self.largeur and 0 <= y < self.hauteur:
            return self.carte[y][x]
        return None
    
    def __str__(self):
        """
        Retourne une représentation textuelle du monde.
        
        Returns:
            str: La représentation textuelle
        """
        return f"Monde: {self.nom} ({self.largeur}x{self.hauteur}, {len(self.rooms)} salles)"

class Room:
    """
    Classe représentant une salle dans le monde du jeu.
    """
    
    def __init__(self, nom, largeur, hauteur, description=""):
        """
        Initialise une nouvelle salle.
        
        Args:
            nom (str): Le nom de la salle
            largeur (int): La largeur de la salle
            hauteur (int): La hauteur de la salle
            description (str, optional): La description de la salle
        """
        self.nom = nom
        self.largeur = largeur
        self.hauteur = hauteur
        self.description = description
        self.position = None  # Position (x, y) dans le monde
        self.personnages = []
        self.items = []
        self.quetes = []
    
    def ajouter_personnage(self, personnage):
        """
        Ajoute un personnage à la salle.
        
        Args:
            personnage (Personnage): Le personnage à ajouter
        """
        self.personnages.append(personnage)
    
    def retirer_personnage(self, personnage):
        """
        Retire un personnage de la salle.
        
        Args:
            personnage (Personnage): Le personnage à retirer
            
        Returns:
            bool: True si le personnage a été retiré avec succès, False sinon
        """
        if personnage in self.personnages:
            self.personnages.remove(personnage)
            return True
        return False
    
    def ajouter_item(self, item):
        """
        Ajoute un item à la salle.
        
        Args:
            item (Item): L'item à ajouter
        """
        self.items.append(item)
    
    def retirer_item(self, item):
        """
        Retire un item de la salle.
        
        Args:
            item (Item): L'item à retirer
            
        Returns:
            bool: True si l'item a été retiré avec succès, False sinon
        """
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def ajouter_quete(self, quete):
        """
        Ajoute une quête à la salle.
        
        Args:
            quete (Quest): La quête à ajouter
        """
        self.quetes.append(quete)
    
    def __str__(self):
        """
        Retourne une représentation textuelle de la salle.
        
        Returns:
            str: La représentation textuelle
        """
        position_str = f" à ({self.position[0]}, {self.position[1]})" if self.position else ""
        return f"{self.nom}{position_str} ({self.largeur}x{self.hauteur})\n{self.description}"
