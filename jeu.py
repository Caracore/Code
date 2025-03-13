import time, dungeon_heroes, dh_data
version = dungeon_heroes.version
save = "save.txt" # voir système de sauvegarde
try:
    with open(save, "r") as f:
        save_exists = True
        print("Charger la Partie")
except FileNotFoundError:
    save_exists = False
    print("Nouvelle Partie")

def new_partie():
    # Initialiser une nouvelle partie
    print("Nouvelle Partie")
    print("- Gamemode")
    gamemode = "easy"  # Par défaut
    difficulty = "easy"  # Par défaut
    
    set_gamemode = input("\nVotre choix: [easy, medium, hard, custom funny] ")
    match set_gamemode:
        case "easy"|"Easy"|"e"|"E":  
            gamemode = "easy"
        case "medium"|"Medium"|"m"|"M":
            gamemode = "medium"
        case "hard"|"Hard"|"h"|"H":
            gamemode = "hard"
        case "custom funny"|"Custom Funny"|"c"|"C"|"custom"|"Custom"|"cf"|"CF":
            gamemode = "custom funny"
            return gamemode, difficulty, ""  # Retourner une chaîne vide pour le nom, il sera défini dans custom_funny
        case _:
            print("\nChoix invalide. Mode easy par défaut.\n")
            time.sleep(1)
    
    print("- Nom de votre personnage")
    name = input("\nVotre nom: ")
    
    return gamemode, difficulty, name

#faire l'histoire etc ...
def presentation():
    print("Bienvenue dans Dungeon Heroes version: " + version)
    status = "Charger la Partie" if save_exists else "Nouvelle Partie(taper: Jouer)"
    print("\nJouer -->\n" + status + "\nParamètres\nSauvegarder\n<-- Quitter\n")
    i_presentation = input("\nVotre choix: ")
    match i_presentation:
        case "Jouer"|"jouer"|"J"|"j"|"1":
            game_instance = story(save_exists)
        case "charger"|"Charger"|"c"|"C"|"2":
            pass #TODO: Charger la partie load save
        case "paramètres"|"Paramètres"|"p"|"P"|"3":
            pass #TODO: Paramètres
        case "sauvegarder"|"Sauvegarder"|"s"|"S"|"4": # ajouter sauvegarder
            pass #TODO: Sauvegarder la partie save
        case "quitter"|"Quitter"|"q"|"Q"|"5": # ajouter sauvegarder
            exit()
        case _:
            print("\nChoix invalide. Veuillez réessayer.\n")
            time.sleep(1)
            presentation()


class story(dungeon_heroes.game):
    def __init__(self, save_exists):
        self.name = ""
        self.vie = 0
        self.attaque = 0
        self.defense = 0
        self.inventaire = []
        self.argent = 0
        
        if save_exists:
            # TODO: Charger les données de sauvegarde
            gamemode, difficulty = "easy", "easy"
            self.name = "Joueur Sauvegardé"
        else:
            gamemode, difficulty, self.name = new_partie()
            
            # Si le mode est custom funny, appeler la méthode custom_funny
            if gamemode == "custom funny":
                self.custom_funny()
        
        super().__init__(gamemode, difficulty)
        
        # Initialiser les attributs du joueur en fonction du mode de jeu
        if self.gamemode == "easy":
            self.vie = 1000
            self.attaque = 100
            self.defense = 100
            self.inventaire = []
            self.argent = 500
        elif self.gamemode == "medium":
            self.vie = 500
            self.attaque = 50
            self.defense = 50
            self.inventaire = []
            self.argent = 250
        elif self.gamemode == "hard":
            self.vie = 250
            self.attaque = 25
            self.defense = 25
            self.inventaire = []
            self.argent = 100
        elif self.gamemode == "custom funny":
            # Les attributs ont déjà été définis dans la méthode custom_funny
            pass
        
        self.start_game()
        
    def menu_potion(self):
        pass #inventaire.append("Potion")
        
    def menu_armure(self):
        pass #inventaire.append("Armure")
        
    def menu_arme(self):
        pass #inventaire.append("Arme")
        
    def menu_autre(self):
        pass  
        
    #CUSTOM FUNNY MENU
    def custom_funny(self):
        print("\n*Custom Funny*")
        print("\nNom de votre personnage")
        name = input("\nVotre nom: ")
        if not name:  # Vérifier si le nom est vide
            print("\nNom invalide. Veuillez réessayer.\n")
            time.sleep(1)
            self.custom_funny()
        else:
            self.name = name
            
        print("\nGamemode")
        print("\nVotre Gamemode est initialisé à custom funny, vous pouvez quasiment tout personnaliser")
        difficulty = input("\nVotre difficulté: [easy, medium, hard] ? ")
        match difficulty:
            case "easy"|"Easy"|"e"|"E":  
                self.difficulty = "easy"
            case "medium"|"Medium"|"m"|"M":
                self.difficulty = "medium"
            case "hard"|"Hard"|"h"|"H":
                self.difficulty = "hard"
            case _:
                print("\nChoix invalide. Difficulté easy par défaut.\n")
                time.sleep(1)
                self.difficulty = "easy"
                
        # Personnalisation des statistiques
        print("\nPersonnalisation des statistiques")
        try:
            self.vie = int(input("\nVie (100-2000): "))
            if self.vie < 100 or self.vie > 2000:
                print("Valeur hors limites. Vie définie à 100.")
                self.vie = 100
        except ValueError:
            print("Valeur invalide. Vie définie à 100.")
            self.vie = 100
            
        try:
            self.attaque = int(input("\nAttaque (10-200): "))
            if self.attaque < 10 or self.attaque > 200:
                print("Valeur hors limites. Attaque définie à 10.")
                self.attaque = 10
        except ValueError:
            print("Valeur invalide. Attaque définie à 10.")
            self.attaque = 10
            
        try:
            self.defense = int(input("\nDéfense (10-200): "))
            if self.defense < 10 or self.defense > 200:
                print("Valeur hors limites. Défense définie à 10.")
                self.defense = 10
        except ValueError:
            print("Valeur invalide. Défense définie à 10.")
            self.defense = 10
            
        try:
            self.argent = int(input("\nArgent (0-1000): "))
            if self.argent < 0 or self.argent > 1000:
                print("Valeur hors limites. Argent défini à 50.")
                self.argent = 50
        except ValueError:
            print("Valeur invalide. Argent défini à 50.")
            self.argent = 50
            
        print("\nPersonnalisation terminée!")
        time.sleep(1)

    def start_game(self):
        print("Début de l'aventure...")
        print(f"Vous êtes {self.name}, vous êtes en mode {self.gamemode}")
        print(f"Avec {self.vie} points de vie, {self.attaque} points d'attaque, {self.defense} points de défense")
        print(f"Inventaire: {self.inventaire}, Argent: {self.argent}")
        print("Ce choix vous convient-il ? [Oui, Non]")
        
        set_start_game = input("\nVotre choix: [Oui, Non] ")
        match set_start_game:
            case "Oui"|"oui"|"o"|"O":
                self.begin_adventure()
            case "Non"|"non"|"n"|"N":
                # Recommencer la création du personnage
                gamemode, difficulty, self.name = new_partie()
                self.__init__(False)  # Réinitialiser avec les nouveaux paramètres
            case _:
                print("\nChoix invalide. Veuillez réessayer.\n")
                time.sleep(1)
                self.start_game()
    
    def begin_adventure(self):
        print("\nVotre aventure commence maintenant...")
        print("Vous vous réveillez dans un petit village nommé Aubétoile, votre tête vous fait mal.")
        print("Vous ne vous souvenez pas comment vous êtes arrivé ici, mais vous savez que vous êtes un aventurier.")
        print("En vous levant, vous remarquez que vous êtes dans une petite auberge. Le tavernier vous regarde avec curiosité.")
        
        print("\n- 'Ah, vous êtes enfin réveillé !' dit-il. 'On vous a trouvé inconscient à l'orée de la forêt hier soir.'")
        print("- 'Vous aviez l'air en mauvais état, mais heureusement rien de grave. Vous vous souvenez de quelque chose ?'")
        
        choix = input("\nQue voulez-vous répondre ? \n1. 'Non, je ne me souviens de rien.' \n2. 'Vaguement... J'étais en mission.' \n3. 'Qui êtes-vous ? Où suis-je ?' \nVotre choix: ")
        
        match choix:
            case "1":
                print("\n- 'Amnésie, hein ? C'est pas de chance,' dit le tavernier en essuyant un verre.")
                print("- 'Mais vous n'êtes pas le premier aventurier à avoir des problèmes près de la forêt ces derniers temps.'")
                print("- 'Il se passe des choses étranges depuis que la vieille tour au nord s'est mise à briller la nuit.'")
                self.explore_village()
            case "2":
                print("\n- 'Une mission ? Intéressant...' Le tavernier vous regarde avec plus d'attention.")
                print("- 'Beaucoup d'aventuriers viennent par ici ces temps-ci, attirés par les rumeurs de trésors dans les ruines.'")
                print("- 'Ou peut-être étiez-vous envoyé pour enquêter sur les disparitions ?'")
                self.explore_village()
            case "3":
                print("\n- 'Du calme, l'ami !' Le tavernier lève les mains. 'Je suis Garen, propriétaire de l'Auberge du Sanglier Doré.'")
                print("- 'Vous êtes à Aubétoile, un petit village à la frontière du royaume. Pas grand-chose à voir ici, mais...'")
                print("- 'Nous avons nos problèmes. Des créatures sortent de la forêt la nuit, et des voyageurs disparaissent.'")
                self.explore_village()
            case _:
                print("\nLe tavernier vous regarde étrangement, ne comprenant pas votre réaction.")
                print("- 'Euh... peut-être que vous avez besoin de vous reposer encore un peu.'")
                self.explore_village()
    
    def explore_village(self):
        print("\nAprès votre conversation avec le tavernier, vous décidez d'explorer le village.")
        print("Aubétoile est un petit village paisible, avec quelques maisons, une forge, un marché et un temple.")
        print("Vous remarquez que les villageois semblent nerveux, jetant régulièrement des regards vers la forêt au nord.")
        
        print("\nOù souhaitez-vous aller ?")
        choix = input("\n1. Visiter la forge \n2. Aller au marché \n3. Se rendre au temple \n4. Explorer les environs du village \nVotre choix: ")
        
        match choix:
            case "1":
                self.visiter_forge()
            case "2":
                self.visiter_marche()
            case "3":
                self.visiter_temple()
            case "4":
                self.explorer_environs()
            case _:
                print("\nVous hésitez, ne sachant pas où aller. Vous décidez de rester sur la place du village pour le moment.")
                self.explore_village()
    
    def visiter_forge(self):
        print("\nVous vous dirigez vers la forge du village. Le forgeron, un homme robuste aux bras musclés, frappe sur une épée incandescente.")
        print("En vous voyant approcher, il s'arrête et essuie son front couvert de sueur.")
        
        print("\n- 'Un nouvel aventurier, hein ?' dit-il. 'Si vous comptez explorer les environs, vous aurez besoin d'équipement.'")
        print("- 'Je peux vous vendre une épée pour 50 pièces d'or, ou une armure pour 75 pièces.'")
        
        # TODO: Implémenter le système d'achat d'équipement
        print("\nCette fonctionnalité sera disponible dans une prochaine mise à jour.")
        self.explore_village()
    
    def visiter_marche(self):
        print("\nVous vous rendez au marché du village. Plusieurs étals proposent des produits frais, des herbes et des potions.")
        print("Une vieille femme vous fait signe d'approcher de son étal rempli de fioles colorées.")
        
        print("\n- 'Vous avez l'air d'un aventurier,' dit-elle avec un sourire édenté. 'J'ai exactement ce qu'il vous faut.'")
        print("- 'Des potions de soin, des élixirs de force, des antidotes... Tout ce dont un héros pourrait avoir besoin !'")
        
        # TODO: Implémenter le système d'achat de potions
        print("\nCette fonctionnalité sera disponible dans une prochaine mise à jour.")
        self.explore_village()
    
    def visiter_temple(self):
        print("\nVous entrez dans le petit temple dédié au dieu de la lumière. L'intérieur est calme et paisible.")
        print("Un prêtre âgé s'approche de vous, son visage marqué par les années mais ses yeux brillants de sagesse.")
        
        print("\n- 'Bienvenue, voyageur,' dit-il doucement. 'Je sens que le destin vous a amené ici pour une raison.'")
        print("- 'Notre village est menacé par une ombre grandissante. Les créatures de la forêt deviennent agressives,'")
        print("- 'et une étrange lueur émane de la vieille tour au nord. Peut-être êtes-vous celui qui pourra nous aider ?'")
        
        print("\nLe prêtre vous propose de vous bénir avant votre départ.")
        choix = input("\nAccepter la bénédiction ? (Oui/Non): ")
        
        if choix.lower() in ["oui", "o", "yes", "y"]:
            print("\nLe prêtre pose ses mains sur votre tête et murmure une prière.")
            print("Vous vous sentez revigoré et prêt à affronter les dangers qui vous attendent.")
            # TODO: Ajouter un bonus temporaire au joueur
        else:
            print("\nVous déclinez poliment l'offre du prêtre, qui hoche la tête avec compréhension.")
        
        self.explore_village()
    
    def explorer_environs(self):
        print("\nVous décidez d'explorer les environs du village. Plusieurs chemins s'offrent à vous:")
        print("Au nord se trouve la forêt dense et mystérieuse, d'où proviendraient les créatures hostiles.")
        print("À l'est, un sentier mène vers les montagnes où se trouvent d'anciennes mines abandonnées.")
        print("À l'ouest, la route continue vers d'autres villages et éventuellement la capitale du royaume.")
        
        choix = input("\nQuelle direction choisissez-vous ? \n1. La forêt au nord \n2. Les mines à l'est \n3. La route à l'ouest \n4. Retourner au village \nVotre choix: ")
        
        match choix:
            case "1":
                print("\nVous vous dirigez vers la forêt. Les arbres deviennent de plus en plus denses, et l'atmosphère plus oppressante.")
                print("Soudain, vous entendez un bruissement dans les buissons...")
                # TODO: Implémenter une rencontre aléatoire ou un combat
                print("\nCette fonctionnalité sera disponible dans une prochaine mise à jour.")
                self.explore_village()
            case "2":
                print("\nVous prenez le chemin vers les mines. Le sentier grimpe à flanc de montagne, offrant une vue sur la vallée.")
                print("À l'entrée des mines, vous remarquez des traces récentes. Quelqu'un ou quelque chose est passé par là...")
                # TODO: Implémenter l'exploration des mines
                print("\nCette fonctionnalité sera disponible dans une prochaine mise à jour.")
                self.explore_village()
            case "3":
                print("\nVous suivez la route vers l'ouest. Après quelques heures de marche, vous croisez une caravane de marchands.")
                print("Ils semblent nerveux et bien armés, inhabituellement méfiants pour de simples commerçants.")
                # TODO: Implémenter une rencontre avec les marchands
                print("\nCette fonctionnalité sera disponible dans une prochaine mise à jour.")
                self.explore_village()
            case "4":
                print("\nVous décidez de retourner au village pour le moment.")
                self.explore_village()
            case _:
                print("\nVous hésitez sur le chemin à prendre et décidez de retourner au village pour réfléchir.")
                self.explore_village()

if __name__ == "__main__":
    presentation()