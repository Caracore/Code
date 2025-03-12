import menu , personnage , personnage_init , item_init , world , quest , time

class Jeu:
    def __init__(self):
        self.menu = menu.Menu()
        self.menu.menu_principal()

if __name__ == "__main__":
    jeu = Jeu()