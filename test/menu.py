import item_init , personnage_init , personnage , world , quest , time # add combat and scenario variables and key input module <---

class Menu:
    def __init__(self):
        pass
    def scene_stepby_step(self, name_list):
        if combat == True:
            input("Appuyez sur Entrée pour continuer le combat...")
        elif scenario == True:
            input("Appuyez sur Entrée pour continuer le scenario...\nOu appuyez sur 'S' pour quitter le scenario.") #TODO: Voir quoi rajouter avec module keyiput, keyboard ? pour mettre la touche S (s).
        else:
            input("Appuyez sur Entrée pour continuer...")
    def menu_creation_personnage(self, name_list):
        self.name_creation = name_list #personnage_init.name
        print("\nCréation du personnage\n")
        self.name_creation = input("Nom du personnage : ")
        print(f"Création du personnage {self.name_creation}")
        if self.name_creation == "":
            print("\nNom invalide. Veuillez réessayer.\n")
            self.menu_creation_personnage(name_list) # (personnage_init.name)
        else:
            return self.name_creation in name_list # personnage_init.name

    def menu_principal(self, name_list=[]):
        while True:
            print("\n" + "=" * 50)
            print(f"{'MENU PRINCIPAL':^50}")
            print("=" * 50 + "\n")
            print("1. Créer un personnage")
            print("2. Charger un personnage") #TODO: Voir quoi rajouter ! et comment faire
            print("3. Quitter")
            
            choix = input("\nVotre choix: ")
            
            if choix == "1":
                self.menu_creation_personnage(name_list) # personnage_init.name
            elif choix == "2":
                pass #TODO: load ?
            elif choix == "3":
                print("\nAu revoir !\n")
                break
            else:
                print("\nChoix invalide. Veuillez réessayer.\n")
                time.sleep(1)
                self.menu_principal()