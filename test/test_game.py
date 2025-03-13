# Importation des classes nécessaires depuis __init__complet.py
from __init__complet import Personnage, Item, PotionSoin, Arme, Armure, Quest, World, Room
import os
import random
import time

class Menu:
    """
    Classe représentant le menu principal du jeu de rôle.
    """
    
    def __init__(self):
        """
        Initialise le menu du jeu.
        """
        self.joueur = None
        self.monde = None
        self.salle_courante = None
        self.ennemis = []
        self.quetes_disponibles = []
        self.quetes_actives = []
        self.quetes_terminees = []
        self.running = True
    
    def effacer_ecran(self):
        """
        Efface l'écran de la console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def attendre(self, secondes=1):
        """
        Fait une pause dans l'exécution.
        
        Args:
            secondes (float): Le nombre de secondes à attendre
        """
        time.sleep(secondes)
    
    def afficher_titre(self, titre):
        """
        Affiche un titre formaté.
        
        Args:
            titre (str): Le titre à afficher
        """
        self.effacer_ecran()
        print("=" * 50)
        print(f"{titre.center(50)}")
        print("=" * 50)
        print()
    
    def afficher_message(self, message):
        """
        Affiche un message avec une pause.
        
        Args:
            message (str): Le message à afficher
        """
        print(message)
        self.attendre(1.5)
    
    def saisir_choix(self, min_val, max_val):
        """
        Demande à l'utilisateur de saisir un choix.
        
        Args:
            min_val (int): La valeur minimale acceptée
            max_val (int): La valeur maximale acceptée
            
        Returns:
            int: Le choix de l'utilisateur
        """
        while True:
            try:
                choix = int(input("Votre choix: "))
                if min_val <= choix <= max_val:
                    return choix
                print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
    
    def initialiser_jeu(self):
        """
        Initialise le jeu avec un monde, un joueur et des quêtes.
        """
        # Création du monde
        self.monde = World("Monde de l'Aventure", 10, 10)
        
        # Création des salles
        village = Room("Village", 2, 2, "Un petit village paisible où vous pouvez vous reposer et faire des achats.")
        foret = Room("Forêt", 3, 3, "Une forêt dense et mystérieuse, habitée par des créatures sauvages.")
        grotte = Room("Grotte", 2, 2, "Une grotte sombre et humide, qui semble abriter d'anciens secrets.")
        montagne = Room("Montagne", 4, 3, "Une chaîne de montagnes escarpées, difficile à traverser mais riche en ressources.")
        
        # Ajout des salles au monde
        self.monde.ajouter_room(village, 0, 0)
        self.monde.ajouter_room(foret, 3, 0)
        self.monde.ajouter_room(grotte, 7, 2)
        self.monde.ajouter_room(montagne, 2, 6)
        
        # Création du joueur
        self.afficher_titre("Création de personnage")
        nom = input("Entrez le nom de votre personnage: ")
        self.joueur = Personnage(nom, vie=100, force=15, defense=10)
        
        # Ajout d'items de base
        potion = PotionSoin("Potion de soin mineure", "Restaure 20 points de vie", 20)
        epee = Arme("Épée en fer", "Une épée solide mais basique", 5)
        bouclier = Armure("Bouclier en bois", "Un bouclier simple qui offre une protection minimale", 3)
        
        self.joueur.ajouter_item(potion)
        self.joueur.ajouter_item(epee)
        self.joueur.ajouter_item(bouclier)
        
        # Création des ennemis
        gobelin = Personnage("Gobelin", vie=50, force=8, defense=3)
        loup = Personnage("Loup sauvage", vie=60, force=10, defense=2)
        bandit = Personnage("Bandit", vie=70, force=12, defense=5)
        troll = Personnage("Troll", vie=120, force=18, defense=8)
        
        # Ajout des ennemis aux salles
        foret.ajouter_personnage(gobelin)
        foret.ajouter_personnage(loup)
        grotte.ajouter_personnage(bandit)
        montagne.ajouter_personnage(troll)
        
        # Création des quêtes
        quete_foret = Quest(
            "La menace de la forêt",
            "Des créatures dangereuses ont été aperçues dans la forêt. Éliminez-les pour assurer la sécurité du village.",
            "Éliminer les créatures de la forêt",
            Arme("Épée enchantée", "Une épée magique qui brille d'une lueur bleue", 10)
        )
        
        quete_grotte = Quest(
            "Les secrets de la grotte",
            "On raconte que la grotte abrite un trésor ancien. Explorez-la et trouvez ce qui s'y cache.",
            "Explorer la grotte et vaincre le bandit",
            PotionSoin("Potion de soin majeure", "Restaure 50 points de vie", 50)
        )
        
        quete_montagne = Quest(
            "Le troll des montagnes",
            "Un troll terrorise les voyageurs qui tentent de traverser les montagnes. Débarrassez-vous de cette menace.",
            "Vaincre le troll des montagnes",
            Armure("Armure en mithril", "Une armure légère mais extrêmement résistante", 15)
        )
        
        # Ajout des quêtes aux salles
        village.ajouter_quete(quete_foret)
        village.ajouter_quete(quete_grotte)
        village.ajouter_quete(quete_montagne)
        
        # Définition de la salle courante
        self.salle_courante = village
        
        # Ajout du joueur à la salle courante
        self.salle_courante.ajouter_personnage(self.joueur)
        
        self.afficher_message(f"Bienvenue dans le monde de l'aventure, {self.joueur.nom}!")
    
    def menu_principal(self):
        """
        Affiche le menu principal du jeu.
        """
        while self.running:
            self.afficher_titre("Menu Principal")
            print(f"Personnage: {self.joueur}")
            print(f"Localisation: {self.salle_courante.nom}")
            print("\nQue souhaitez-vous faire?")
            print("1. Explorer")
            print("2. Combattre")
            print("3. Consulter les quêtes")
            print("4. Gérer l'inventaire")
            print("5. Voyager")
            print("6. Se reposer (sauvegarder)")
            print("7. Quitter le jeu")
            
            choix = self.saisir_choix(1, 7)
            
            if choix == 1:
                self.menu_exploration()
            elif choix == 2:
                self.menu_combat()
            elif choix == 3:
                self.menu_quetes()
            elif choix == 4:
                self.menu_inventaire()
            elif choix == 5:
                self.menu_voyage()
            elif choix == 6:
                self.se_reposer()
            elif choix == 7:
                self.quitter_jeu()
    
    def menu_exploration(self):
        """
        Affiche le menu d'exploration de la salle courante.
        """
        self.afficher_titre(f"Exploration: {self.salle_courante.nom}")
        print(self.salle_courante.description)
        
        # Afficher les personnages présents
        if len(self.salle_courante.personnages) > 1:  # > 1 car le joueur est déjà dans la liste
            print("\nPersonnages présents:")
            for personnage in self.salle_courante.personnages:
                if personnage != self.joueur:
                    print(f"- {personnage}")
        
        # Afficher les items présents
        if self.salle_courante.items:
            print("\nObjets trouvés:")
            for i, item in enumerate(self.salle_courante.items):
                print(f"{i+1}. {item}")
            
            print("\nQue souhaitez-vous faire?")
            print("1. Ramasser un objet")
            print("2. Retour au menu principal")
            
            choix = self.saisir_choix(1, 2)
            
            if choix == 1 and self.salle_courante.items:
                print("\nQuel objet souhaitez-vous ramasser?")
                for i, item in enumerate(self.salle_courante.items):
                    print(f"{i+1}. {item}")
                
                choix_item = self.saisir_choix(1, len(self.salle_courante.items))
                item = self.salle_courante.items[choix_item - 1]
                self.joueur.ajouter_item(item)
                self.salle_courante.retirer_item(item)
                self.afficher_message(f"Vous avez ramassé: {item.nom}")
        else:
            print("\nAucun objet à ramasser.")
            self.attendre(2)
    
    def menu_combat(self):
        """
        Affiche le menu de combat.
        """
        # Vérifier s'il y a des ennemis dans la salle
        ennemis = [p for p in self.salle_courante.personnages if p != self.joueur]
        
        if not ennemis:
            self.afficher_message("Il n'y a personne à combattre ici.")
            return
        
        self.afficher_titre("Combat")
        print("Ennemis présents:")
        for i, ennemi in enumerate(ennemis):
            print(f"{i+1}. {ennemi}")
        
        print("\nQui souhaitez-vous attaquer?")
        print(f"{len(ennemis) + 1}. Retour au menu principal")
        
        choix = self.saisir_choix(1, len(ennemis) + 1)
        
        if choix <= len(ennemis):
            ennemi = ennemis[choix - 1]
            self.combat(ennemi)
    
    def combat(self, ennemi):
        """
        Gère un combat entre le joueur et un ennemi.
        
        Args:
            ennemi (Personnage): L'ennemi à combattre
        """
        self.afficher_titre(f"Combat contre {ennemi.nom}")
        
        tour = 1
        while self.joueur.vie > 0 and ennemi.vie > 0:
            print(f"\nTour {tour}")
            print(f"{self.joueur.nom}: {self.joueur.vie}/{self.joueur.max_vie} PV")
            print(f"{ennemi.nom}: {ennemi.vie}/{ennemi.max_vie} PV")
            
            print("\nQue souhaitez-vous faire?")
            print("1. Attaquer")
            print("2. Utiliser un objet")
            print("3. Fuir")
            
            choix = self.saisir_choix(1, 3)
            
            if choix == 1:
                # Attaque du joueur
                degats = self.joueur.attaquer(ennemi)
                self.afficher_message(f"Vous infligez {degats} points de dégâts à {ennemi.nom}!")
                
                # Vérifier si l'ennemi est vaincu
                if ennemi.vie <= 0:
                    self.afficher_message(f"Vous avez vaincu {ennemi.nom}!")
                    self.salle_courante.retirer_personnage(ennemi)
                    
                    # Vérifier si une quête est complétée
                    for quete in self.quetes_actives:
                        if "Éliminer" in quete.objectif or "Vaincre" in quete.objectif:
                            if ennemi.nom.lower() in quete.objectif.lower():
                                recompense = quete.completer()
                                self.quetes_actives.remove(quete)
                                self.quetes_terminees.append(quete)
                                if recompense:
                                    self.joueur.ajouter_item(recompense)
                                    self.afficher_message(f"Quête complétée! Vous recevez: {recompense.nom}")
                                else:
                                    self.afficher_message(f"Quête complétée!")
                    
                    break
                
                # Attaque de l'ennemi
                degats = ennemi.attaquer(self.joueur)
                self.afficher_message(f"{ennemi.nom} vous inflige {degats} points de dégâts!")
                
                # Vérifier si le joueur est vaincu
                if self.joueur.vie <= 0:
                    self.afficher_message("Vous avez été vaincu! Game Over!")
                    self.running = False
                    break
            
            elif choix == 2:
                # Utiliser un objet
                if not self.joueur.inventaire:
                    self.afficher_message("Votre inventaire est vide!")
                    continue
                
                print("\nQuel objet souhaitez-vous utiliser?")
                for i, item in enumerate(self.joueur.inventaire):
                    print(f"{i+1}. {item}")
                print(f"{len(self.joueur.inventaire) + 1}. Retour au combat")
                
                choix_item = self.saisir_choix(1, len(self.joueur.inventaire) + 1)
                
                if choix_item <= len(self.joueur.inventaire):
                    if self.joueur.utiliser_item(choix_item - 1):
                        self.afficher_message(f"Vous utilisez {self.joueur.inventaire[choix_item - 1].nom}")
                    else:
                        self.afficher_message("Impossible d'utiliser cet objet!")
                
                # Attaque de l'ennemi
                degats = ennemi.attaquer(self.joueur)
                self.afficher_message(f"{ennemi.nom} vous inflige {degats} points de dégâts!")
                
                # Vérifier si le joueur est vaincu
                if self.joueur.vie <= 0:
                    self.afficher_message("Vous avez été vaincu! Game Over!")
                    self.running = False
                    break
            
            elif choix == 3:
                # Fuir le combat
                chance_fuite = random.random()
                if chance_fuite > 0.3:  # 70% de chance de fuir
                    self.afficher_message("Vous parvenez à fuir le combat!")
                    break
                else:
                    self.afficher_message("Vous ne parvenez pas à fuir!")
                    
                    # Attaque de l'ennemi
                    degats = ennemi.attaquer(self.joueur)
                    self.afficher_message(f"{ennemi.nom} vous inflige {degats} points de dégâts!")
                    
                    # Vérifier si le joueur est vaincu
                    if self.joueur.vie <= 0:
                        self.afficher_message("Vous avez été vaincu! Game Over!")
                        self.running = False
                        break
            
            tour += 1
    
    def menu_quetes(self):
        """
        Affiche le menu de gestion des quêtes.
        """
        while True:
            self.afficher_titre("Quêtes")
            
            # Récupérer les quêtes disponibles dans la salle courante
            quetes_disponibles = [q for q in self.salle_courante.quetes if q not in self.quetes_actives and q not in self.quetes_terminees]
            
            print("1. Quêtes disponibles")
            print("2. Quêtes actives")
            print("3. Quêtes terminées")
            print("4. Retour au menu principal")
            
            choix = self.saisir_choix(1, 4)
            
            if choix == 1:
                self.afficher_titre("Quêtes disponibles")
                if quetes_disponibles:
                    for i, quete in enumerate(quetes_disponibles):
                        print(f"{i+1}. {quete.titre}")
                    
                    print(f"\nQuelle quête souhaitez-vous consulter?")
                    print(f"{len(quetes_disponibles) + 1}. Retour")
                    
                    choix_quete = self.saisir_choix(1, len(quetes_disponibles) + 1)
                    
                    if choix_quete <= len(quetes_disponibles):
                        quete = quetes_disponibles[choix_quete - 1]
                        self.afficher_titre(quete.titre)
                        print(quete.description)
                        print(f"Objectif: {quete.objectif}")
                        if quete.recompense:
                            print(f"Récompense: {quete.recompense.nom}")
                        
                        print("\nAccepter cette quête?")
                        print("1. Oui")
                        print("2. Non")
                        
                        choix_accepter = self.saisir_choix(1, 2)
                        
                        if choix_accepter == 1:
                            self.quetes_actives.append(quete)
                            self.afficher_message("Quête acceptée!")
                else:
                    self.afficher_message("Aucune quête disponible dans cette zone.")
            
            elif choix == 2:
                self.afficher_titre("Quêtes actives")
                if self.quetes_actives:
                    for i, quete in enumerate(self.quetes_actives):
                        print(f"{i+1}. {quete.titre}")
                    
                    print(f"\nQuelle quête souhaitez-vous consulter?")
                    print(f"{len(self.quetes_actives) + 1}. Retour")
                    
                    choix_quete = self.saisir_choix(1, len(self.quetes_actives) + 1)
                    
                    if choix_quete <= len(self.quetes_actives):
                        quete = self.quetes_actives[choix_quete - 1]
                        self.afficher_titre(quete.titre)
                        print(quete.description)
                        print(f"Objectif: {quete.objectif}")
                        if quete.recompense:
                            print(f"Récompense: {quete.recompense.nom}")
                        
                        print("\nAppuyez sur Entrée pour continuer...")
                        input()
                else:
                    self.afficher_message("Vous n'avez aucune quête active.")
            
            elif choix == 3:
                self.afficher_titre("Quêtes terminées")
                if self.quetes_terminees:
                    for i, quete in enumerate(self.quetes_terminees):
                        print(f"{i+1}. {quete.titre}")
                    
                    print(f"\nQuelle quête souhaitez-vous consulter?")
                    print(f"{len(self.quetes_terminees) + 1}. Retour")
                    
                    choix_quete = self.saisir_choix(1, len(self.quetes_terminees) + 1)
                    
                    if choix_quete <= len(self.quetes_terminees):
                        quete = self.quetes_terminees[choix_quete - 1]
                        self.afficher_titre(quete.titre)
                        print(quete.description)
                        print(f"Objectif: {quete.objectif}")
                        if quete.recompense:
                            print(f"Récompense: {quete.recompense.nom}")
                        print("Statut: Complétée")
                        
                        print("\nAppuyez sur Entrée pour continuer...")
                        input()
                else:
                    self.afficher_message("Vous n'avez terminé aucune quête.")
            
            elif choix == 4:
                break
    
    def menu_inventaire(self):
        """
        Affiche le menu de gestion de l'inventaire.
        """
        while True:
            self.afficher_titre("Inventaire")
            
            if self.joueur.inventaire:
                for i, item in enumerate(self.joueur.inventaire):
                    print(f"{i+1}. {item}")
                
                print("\nQue souhaitez-vous faire?")
                print("1. Utiliser un objet")
                print("2. Examiner un objet")
                print("3. Jeter un objet")
                print("4. Retour au menu principal")
                
                choix = self.saisir_choix(1, 4)
                
                if choix == 1:
                    print("\nQuel objet souhaitez-vous utiliser?")
                    choix_item = self.saisir_choix(1, len(self.joueur.inventaire))
                    
                    if self.joueur.utiliser_item(choix_item - 1):
                        self.afficher_message(f"Vous utilisez {self.joueur.inventaire[choix_item - 1].nom}")
                    else:
                        self.afficher_message("Impossible d'utiliser cet objet!")
                
                elif choix == 2:
                    print("\nQuel objet souhaitez-vous examiner?")
                    choix_item = self.saisir_choix(1, len(self.joueur.inventaire))
                    
                    item = self.joueur.inventaire[choix_item - 1]
                    self.afficher_titre(item.nom)
                    print(item.description)
                    
                    if isinstance(item, PotionSoin):
                        print(f"Soigne {item.puissance} points de vie")
                    elif isinstance(item, Arme):
                        print(f"Bonus de force: +{item.bonus_force}")
                    elif isinstance(item, Armure):
                        print(f"Bonus de défense: +{item.bonus_defense}")
                    
                    print("\nAppuyez sur Entrée pour continuer...")
                    input()
                
                elif choix == 3:
                    print("\nQuel objet souhaitez-vous jeter?")
                    choix_item = self.saisir_choix(1, len(self.joueur.inventaire))
                    
                    item = self.joueur.inventaire.pop(choix_item - 1)
                    self.salle_courante.ajouter_item(item)
                    self.afficher_message(f"Vous jetez {item.nom}")
                
                elif choix == 4:
                    break
            else:
                self.afficher_message("Votre inventaire est vide!")
                break
    
    def menu_voyage(self):
        """
        Affiche le menu de voyage entre les salles.
        """
        self.afficher_titre("Voyage")
        
        # Trouver les salles adjacentes
        salles_adjacentes = []
        position_actuelle = self.salle_courante.position
        
        if not position_actuelle:
            self.afficher_message("Erreur: Position actuelle inconnue!")
            return
        
        x, y = position_actuelle
        
        # Vérifier les quatre directions
        directions = [
            ("Nord", x, y - 1),
            ("Est", x + 1, y),
            ("Sud", x, y + 1),
            ("Ouest", x - 1, y)
        ]
        
        for direction, new_x, new_y in directions:
            salle = self.monde.obtenir_room(new_x, new_y)
            if salle:
                salles_adjacentes.append((direction, salle))
        
        if salles_adjacentes:
            print("Destinations possibles:")
            for i, (direction, salle) in enumerate(salles_adjacentes):
                print(f"{i+1}. {direction}: {salle.nom}")
            
            print(f"{len(salles_adjacentes) + 1}. Rester ici")
            
            choix = self.saisir_choix(1, len(salles_adjacentes) + 1)
            
            if choix <= len(salles_adjacentes):
                direction, nouvelle_salle = salles_adjacentes[choix - 1]
                
                # Retirer le joueur de la salle actuelle
                self.salle_courante.retirer_personnage(self.joueur)
                
                # Mettre à jour la salle courante
                self.salle_courante = nouvelle_salle
                
                # Ajouter le joueur à la nouvelle salle
                self.salle_courante.ajouter_personnage(self.joueur)
                
                self.afficher_message(f"Vous voyagez vers {direction} et arrivez à {nouvelle_salle.nom}.")
        else:
            self.afficher_message("Il n'y a aucune destination accessible depuis votre position actuelle.")
    
    def se_reposer(self):
        """
        Permet au joueur de se reposer pour récupérer des points de vie.
        """
        self.afficher_titre("Repos")
        
        if self.joueur.vie < self.joueur.max_vie:
            recuperation = min(self.joueur.max_vie - self.joueur.vie, 20)  # Récupère jusqu'à 20 PV
            self.joueur.soigner(recuperation)
            self.afficher_message(f"Vous vous reposez et récupérez {recuperation} points de vie.")
            save_input = input("Voulez-vous sauvegarder votre partie ? (o/n) ")
            if save_input.lower() == "o":
                self.sauvegarder()
            elif save_input.lower() == "n":
                self.afficher_message("Vous n'avez pas sauvegardé votre partie.")
            else:
                self.afficher_message("Veuillez entrer 'o' ou 'n'.")
        else:
            self.afficher_message("Vous êtes déjà en pleine forme!")

    def sauvegarder(self):
        """
        Sauvegarde l'état actuel du jeu dans un fichier.
        """
        import pickle
        import datetime
        
        self.afficher_titre("Sauvegarde")
        
        # Créer le dossier de sauvegarde s'il n'existe pas
        if not os.path.exists("sauvegardes"):
            os.makedirs("sauvegardes")
        
        # Générer un nom de fichier avec la date et l'heure
        date_heure = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nom_fichier = f"sauvegardes/{self.joueur.nom}_{date_heure}.save"

        # Préparer les données à sauvegarder
        donnees = {
            "joueur": {
                "nom": self.joueur.nom,
                "vie": self.joueur.vie,
                "max_vie": self.joueur.max_vie,
                "force": self.joueur.force,
                "defense": self.joueur.defense,
                "inventaire": [(item.nom, item.description) for item in self.joueur.inventaire]
            },
            "monde": {
                "nom": self.monde.nom,
                "largeur": self.monde.largeur,
                "hauteur": self.monde.hauteur
            },
            "salle_courante": {
                "nom": self.salle_courante.nom,
                "position": self.salle_courante.position
            },
            "quetes_actives": [(q.titre, q.description, q.objectif) for q in self.quetes_actives],
            "quetes_terminees": [(q.titre, q.description, q.objectif) for q in self.quetes_terminees]
        }

        try:
            with open(nom_fichier, "wb") as fichier:
                pickle.dump(donnees, fichier)
            self.afficher_message(f"Partie sauvegardée avec succès dans {nom_fichier}")
            return True
        except Exception as e:
            self.afficher_message(f"Erreur lors de la sauvegarde: {str(e)}")
            return False
            
    def quitter_jeu(self):
        """
        Quitte le jeu.
        """
        self.afficher_titre("Quitter le jeu")
        print("Êtes-vous sûr de vouloir quitter le jeu?")
        print("1. Oui")
        print("2. Non")
        
        choix = self.saisir_choix(1, 2)
        
        if choix == 1:
            self.afficher_message("Merci d'avoir joué! À bientôt!")
            self.running = False

    def charger(self):
        """
        Charge une partie sauvegardée.
        
        Returns:
            bool: True si le chargement a réussi, False sinon
        """
        import pickle
        import glob
        
        self.afficher_titre("Chargement")
        
        # Vérifier si le dossier de sauvegarde existe
        if not os.path.exists("sauvegardes"):
            self.afficher_message("Aucune sauvegarde trouvée.")
            return False
        
        # Récupérer la liste des fichiers de sauvegarde
        sauvegardes = glob.glob("sauvegardes/*.save")

        if not sauvegardes:
            self.afficher_message("Aucune sauvegarde trouvée.")
            return False

        # Afficher les sauvegardes disponibles
        print("Sauvegardes disponibles:")
        for i, sauvegarde in enumerate(sauvegardes):
            nom_fichier = os.path.basename(sauvegarde)
            print(f"{i+1}. {nom_fichier}")

        print(f"{len(sauvegardes) + 1}. Retour")

        choix = self.saisir_choix(1, len(sauvegardes) + 1)

        if choix > len(sauvegardes):
            return False

        # Charger la sauvegarde sélectionnée
        try:
            with open(sauvegardes[choix - 1], "rb") as fichier:
                donnees = pickle.load(fichier)
            
            # Recréer l'état du jeu
            self.initialiser_jeu()  # Initialiser le jeu de base
            
            # Mettre à jour le joueur
            self.joueur.nom = donnees["joueur"]["nom"]
            self.joueur.vie = donnees["joueur"]["vie"]
            self.joueur.max_vie = donnees["joueur"]["max_vie"]
            self.joueur.force = donnees["joueur"]["force"]
            self.joueur.defense = donnees["joueur"]["defense"]
            
            # Trouver la salle courante
            for room in self.monde.rooms:
                if room.nom == donnees["salle_courante"]["nom"]:
                    # Retirer le joueur de la salle actuelle
                    self.salle_courante.retirer_personnage(self.joueur)
                    # Mettre à jour la salle courante
                    self.salle_courante = room
                    # Ajouter le joueur à la nouvelle salle
                    self.salle_courante.ajouter_personnage(self.joueur)
                    break
            
            # Restaurer les quêtes (simplifié)
            # Note: Cette partie est simplifiée et pourrait être améliorée
            # pour restaurer complètement l'état des quêtes
            
            self.afficher_message(f"Partie chargée avec succès!")
            return True
        except Exception as e:
            self.afficher_message(f"Erreur lors du chargement: {str(e)}")
            return False

    def demarrer(self):
        """
        Démarre le jeu.
        """
        self.afficher_titre("Bienvenue dans l'Aventure RPG")
        print("1. Nouvelle partie")
        print("2. Charger une partie")
        print("3. Quitter")
        
        choix = self.saisir_choix(1, 3)
        
        if choix == 1:
            self.initialiser_jeu()
            self.menu_principal()
        elif choix == 2:
            if self.charger():
                self.menu_principal()
            else:
                self.demarrer()
        else:
            self.afficher_message("À bientôt!")

# Point d'entrée du programme
if __name__ == "__main__":
    jeu = Menu()
    jeu.demarrer()