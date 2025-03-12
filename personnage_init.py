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
