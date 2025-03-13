import dungeon_heroes

# Data
class data():

    class monstre_s(dungeon_heroes.monstre):
        def __init__(self, nom, vie, attaque, defense, inventaire):
            super().__init__("spider", vie, attaque, defense, inventaire)
            pass

    class monstre_m(dungeon_heroes.monstre):
        def __init__(self, nom, vie, attaque, defense, inventaire):
            super().__init__(nom, vie, attaque, defense, inventaire)
            pass

    class monstre_l(dungeon_heroes.monstre):
        def __init__(self, nom, vie, attaque, defense, inventaire):
            super().__init__(nom, vie, attaque, defense, inventaire)
            pass
    
    class donjon_level(dungeon_heroes.donjon): #dungeon name
        def __init__(self, nom, d_difficulty, d_loot, d_monstre, d_item):  # d_loot voir le loot potentiel
            super().__init__(nom, d_difficulty, d_loot, d_monstre, d_item) # rajouter le level du donjon (easy, medium, hard) / au mode cutom funny or donjon level hardcore ajouter level au personnage et faire une boucle infini avec chance de spawn le boss pour sortir du donjon. 
            pass

    class village_name(dungeon_heroes.village): #village name each village, 1er village
        def __init__(self, nom, v_difficulty, v_loot, v_monstre, v_item):  # v_loot voir le loot potentiel
            super().__init__(nom, v_difficulty, v_loot, v_monstre, v_item) # rajouter le level du village (easy, medium, hard) / au mode cutom funny or village level hardcore ajouter level au personnage et faire une boucle infini avec chance de spawn le boss pour sortir du village. 
            pass