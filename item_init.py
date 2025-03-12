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