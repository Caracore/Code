import tkinter as tk, dungeon_heroes, dh_data
from tkinter import ttk, scrolledtext, messagebox
import random
import time

# Version du jeu
VERSION = "1.0.0"

class DungeonHeroesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(f"Dungeon Heroes - v{VERSION}")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Attributs du joueur
        self.player_name = ""
        self.gamemode = "easy"
        self.difficulty = "easy"
        self.health = 100
        self.attack = 10
        self.defense = 10
        self.inventory = []
        self.gold = 50
        
        # État du jeu
        self.game_state = "MENU"  # MENU, CHARACTER_CREATION, GAME, COMBAT, INVENTORY
        
        # Création de l'interface
        self.create_widgets()
        self.show_main_menu()
        
    def create_widgets(self):
        # Frame principal
        self.main_frame = tk.Frame(self.root, bg="#2c3e50")
        self.main_frame.pack(fill="both", expand=True)
        
        # Zone de texte pour les messages du jeu
        self.text_frame = tk.Frame(self.main_frame, bg="#34495e")
        self.text_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.game_text = scrolledtext.ScrolledText(self.text_frame, wrap=tk.WORD, 
                                                 width=80, height=20, 
                                                 bg="#2c3e50", fg="white",
                                                 font=("Helvetica", 12))
        self.game_text.pack(fill="both", expand=True, padx=10, pady=10)
        self.game_text.config(state=tk.DISABLED)
        
        # Frame pour les boutons
        self.button_frame = tk.Frame(self.main_frame, bg="#34495e")
        self.button_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Frame pour les statistiques du joueur
        self.stats_frame = tk.Frame(self.main_frame, bg="#34495e")
        self.stats_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Labels pour les statistiques
        self.name_label = tk.Label(self.stats_frame, text="Nom: -", bg="#34495e", fg="white", font=("Helvetica", 10))
        self.name_label.pack(side=tk.LEFT, padx=10)
        
        self.health_label = tk.Label(self.stats_frame, text="Vie: -", bg="#34495e", fg="white", font=("Helvetica", 10))
        self.health_label.pack(side=tk.LEFT, padx=10)
        
        self.attack_label = tk.Label(self.stats_frame, text="Attaque: -", bg="#34495e", fg="white", font=("Helvetica", 10))
        self.attack_label.pack(side=tk.LEFT, padx=10)
        
        self.defense_label = tk.Label(self.stats_frame, text="Défense: -", bg="#34495e", fg="white", font=("Helvetica", 10))
        self.defense_label.pack(side=tk.LEFT, padx=10)
        
        self.gold_label = tk.Label(self.stats_frame, text="Or: -", bg="#34495e", fg="white", font=("Helvetica", 10))
        self.gold_label.pack(side=tk.LEFT, padx=10)
        
        # Cacher les statistiques au démarrage
        self.stats_frame.pack_forget()
    
    def update_stats_display(self):
        self.name_label.config(text=f"Nom: {self.player_name}")
        self.health_label.config(text=f"Vie: {self.health}")
        self.attack_label.config(text=f"Attaque: {self.attack}")
        self.defense_label.config(text=f"Défense: {self.defense}")
        self.gold_label.config(text=f"Or: {self.gold}")
    
    def clear_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()
    
    def print_text(self, text):
        self.game_text.config(state=tk.NORMAL)
        self.game_text.insert(tk.END, text + "\n")
        self.game_text.see(tk.END)
        self.game_text.config(state=tk.DISABLED)
    
    def clear_text(self):
        self.game_text.config(state=tk.NORMAL)
        self.game_text.delete(1.0, tk.END)
        self.game_text.config(state=tk.DISABLED)
    
    def show_main_menu(self):
        self.game_state = "MENU"
        self.clear_text()
        self.clear_buttons()
        self.stats_frame.pack_forget()
        
        self.print_text(f"Bienvenue dans Dungeon Heroes version: {VERSION}")
        self.print_text("\nUn jeu d'aventure où vous incarnez un héros dans un monde fantastique.")
        self.print_text("\nQue souhaitez-vous faire ?")
        
        # Boutons du menu principal
        new_game_btn = tk.Button(self.button_frame, text="Nouvelle Partie", 
                               command=self.start_new_game,
                               bg="#3498db", fg="white", font=("Helvetica", 12),
                               width=15, height=2)
        new_game_btn.pack(side=tk.LEFT, padx=10, pady=10)
        
        load_game_btn = tk.Button(self.button_frame, text="Charger Partie",
                                command=self.load_game,
                                bg="#3498db", fg="white", font=("Helvetica", 12),
                                width=15, height=2)
        load_game_btn.pack(side=tk.LEFT, padx=10, pady=10)
        
        settings_btn = tk.Button(self.button_frame, text="Paramètres",
                               command=self.show_settings,
                               bg="#3498db", fg="white", font=("Helvetica", 12),
                               width=15, height=2)
        settings_btn.pack(side=tk.LEFT, padx=10, pady=10)
        
        quit_btn = tk.Button(self.button_frame, text="Quitter",
                           command=self.root.quit,
                           bg="#e74c3c", fg="white", font=("Helvetica", 12),
                           width=15, height=2)
        quit_btn.pack(side=tk.LEFT, padx=10, pady=10)
    
    def start_new_game(self):
        self.game_state = "CHARACTER_CREATION"
        self.clear_text()
        self.clear_buttons()
        
        self.print_text("Création de personnage")
        self.print_text("\nComment vous appelez-vous, aventurier ?")
        
        # Frame pour l'entrée du nom
        name_frame = tk.Frame(self.button_frame, bg="#34495e")
        name_frame.pack(fill="x", padx=10, pady=10)
        
        name_label = tk.Label(name_frame, text="Nom:", bg="#34495e", fg="white", font=("Helvetica", 12))
        name_label.pack(side=tk.LEFT, padx=5)
        
        self.name_entry = tk.Entry(name_frame, font=("Helvetica", 12), width=20)
        self.name_entry.pack(side=tk.LEFT, padx=5)
        self.name_entry.focus_set()
        
        # Frame pour les boutons de difficulté
        diff_frame = tk.Frame(self.button_frame, bg="#34495e")
        diff_frame.pack(fill="x", padx=10, pady=10)
        
        diff_label = tk.Label(diff_frame, text="Difficulté:", bg="#34495e", fg="white", font=("Helvetica", 12))
        diff_label.pack(side=tk.LEFT, padx=5)
        
        easy_btn = tk.Button(diff_frame, text="Facile", 
                           command=lambda: self.set_difficulty("easy"),
                           bg="#2ecc71", fg="white", font=("Helvetica", 10),
                           width=8)
        easy_btn.pack(side=tk.LEFT, padx=5)
        
        medium_btn = tk.Button(diff_frame, text="Moyen", 
                             command=lambda: self.set_difficulty("medium"),
                             bg="#f39c12", fg="white", font=("Helvetica", 10),
                             width=8)
        medium_btn.pack(side=tk.LEFT, padx=5)
        
        hard_btn = tk.Button(diff_frame, text="Difficile", 
                           command=lambda: self.set_difficulty("hard"),
                           bg="#e74c3c", fg="white", font=("Helvetica", 10),
                           width=8)
        hard_btn.pack(side=tk.LEFT, padx=5)
        
        custom_btn = tk.Button(diff_frame, text="Personnalisé", 
                             command=lambda: self.set_difficulty("custom funny"),
                             bg="#9b59b6", fg="white", font=("Helvetica", 10),
                             width=10)
        custom_btn.pack(side=tk.LEFT, padx=5)
        
        # Bouton de confirmation
        confirm_btn = tk.Button(self.button_frame, text="Commencer l'aventure", 
                              command=self.confirm_character,
                              bg="#3498db", fg="white", font=("Helvetica", 12),
                              width=20, height=2)
        confirm_btn.pack(pady=10)
        
        # Bouton retour
        back_btn = tk.Button(self.button_frame, text="Retour", 
                           command=self.show_main_menu,
                           bg="#7f8c8d", fg="white", font=("Helvetica", 10))
        back_btn.pack(pady=5)
    
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.gamemode = difficulty
        
        if difficulty == "custom funny":
            self.show_custom_settings()
        else:
            # Définir les statistiques en fonction de la difficulté
            if difficulty == "easy":
                self.health = 1000
                self.attack = 100
                self.defense = 100
                self.gold = 500
            elif difficulty == "medium":
                self.health = 500
                self.attack = 50
                self.defense = 50
                self.gold = 250
            elif difficulty == "hard":
                self.health = 250
                self.attack = 25
                self.defense = 25
                self.gold = 100
    
    def show_custom_settings(self):
        custom_window = tk.Toplevel(self.root)
        custom_window.title("Paramètres personnalisés")
        custom_window.geometry("400x300")
        custom_window.resizable(False, False)
        custom_window.configure(bg="#2c3e50")
        
        # Frame pour les entrées
        entry_frame = tk.Frame(custom_window, bg="#2c3e50")
        entry_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Vie
        health_label = tk.Label(entry_frame, text="Vie (100-2000):", bg="#2c3e50", fg="white", font=("Helvetica", 12))
        health_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        health_entry = tk.Entry(entry_frame, font=("Helvetica", 12), width=10)
        health_entry.grid(row=0, column=1, padx=5, pady=5)
        health_entry.insert(0, "100")
        
        # Attaque
        attack_label = tk.Label(entry_frame, text="Attaque (10-200):", bg="#2c3e50", fg="white", font=("Helvetica", 12))
        attack_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
        attack_entry = tk.Entry(entry_frame, font=("Helvetica", 12), width=10)
        attack_entry.grid(row=1, column=1, padx=5, pady=5)
        attack_entry.insert(0, "10")
        
        # Défense
        defense_label = tk.Label(entry_frame, text="Défense (10-200):", bg="#2c3e50", fg="white", font=("Helvetica", 12))
        defense_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        
        defense_entry = tk.Entry(entry_frame, font=("Helvetica", 12), width=10)
        defense_entry.grid(row=2, column=1, padx=5, pady=5)
        defense_entry.insert(0, "10")
        
        # Or
        gold_label = tk.Label(entry_frame, text="Or (0-1000):", bg="#2c3e50", fg="white", font=("Helvetica", 12))
        gold_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        
        gold_entry = tk.Entry(entry_frame, font=("Helvetica", 12), width=10)
        gold_entry.grid(row=3, column=1, padx=5, pady=5)
        gold_entry.insert(0, "50")
        
        # Bouton de confirmation
        def confirm_custom():
            try:
                health = int(health_entry.get())
                attack = int(attack_entry.get())
                defense = int(defense_entry.get())
                gold = int(gold_entry.get())
                
                # Vérification des valeurs
                if not (100 <= health <= 2000):
                    messagebox.showwarning("Valeur incorrecte", "La vie doit être entre 100 et 2000.")
                    return
                
                if not (10 <= attack <= 200):
                    messagebox.showwarning("Valeur incorrecte", "L'attaque doit être entre 10 et 200.")
                    return
                
                if not (10 <= defense <= 200):
                    messagebox.showwarning("Valeur incorrecte", "La défense doit être entre 10 et 200.")
                    return
                
                if not (0 <= gold <= 1000):
                    messagebox.showwarning("Valeur incorrecte", "L'or doit être entre 0 et 1000.")
                    return
                
                # Définir les statistiques
                self.health = health
                self.attack = attack
                self.defense = defense
                self.gold = gold
                
                custom_window.destroy()
                
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")
        
        confirm_btn = tk.Button(entry_frame, text="Confirmer", 
                              command=confirm_custom,
                              bg="#3498db", fg="white", font=("Helvetica", 12),
                              width=15)
        confirm_btn.grid(row=4, column=0, columnspan=2, pady=20)
    
    def confirm_character(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Nom manquant", "Veuillez entrer un nom pour votre personnage.")
            return
        
        self.player_name = name
        self.update_stats_display()
        self.begin_adventure()
    
    def load_game(self):
        # Fonctionnalité à implémenter
        messagebox.showinfo("Information", "La fonctionnalité de chargement sera disponible dans une prochaine mise à jour.")
    
    def show_settings(self):
        # Fonctionnalité à implémenter
        messagebox.showinfo("Information", "Les paramètres seront disponibles dans une prochaine mise à jour.")
    
    def begin_adventure(self):
        self.game_state = "GAME"
        self.clear_text()
        self.clear_buttons()
        
        # Afficher les statistiques
        self.stats_frame.pack(fill="x", padx=20, pady=(0, 20))
        self.update_stats_display()
        
        self.print_text("Votre aventure commence maintenant...")
        self.print_text(f"Vous êtes {self.player_name}, un aventurier en quête de gloire et de richesses.")
        self.print_text("\nVous vous réveillez dans un petit village nommé Aubétoile, votre tête vous fait mal.")
        self.print_text("Vous ne vous souvenez pas comment vous êtes arrivé ici, mais vous savez que vous êtes un aventurier.")
        self.print_text("En vous levant, vous remarquez que vous êtes dans une petite auberge. Le tavernier vous regarde avec curiosité.")
        
        self.print_text("\n- 'Ah, vous êtes enfin réveillé !' dit-il. 'On vous a trouvé inconscient à l'orée de la forêt hier soir.'")
        self.print_text("- 'Vous aviez l'air en mauvais état, mais heureusement rien de grave. Vous vous souvenez de quelque chose ?'")
        
        # Boutons de choix de dialogue
        btn1 = tk.Button(self.button_frame, text="'Non, je ne me souviens de rien.'", 
                       command=lambda: self.tavern_dialogue(1),
                       bg="#3498db", fg="white", font=("Helvetica", 10),
                       wraplength=150)
        btn1.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
        
        btn2 = tk.Button(self.button_frame, text="'Vaguement... J'étais en mission.'", 
                       command=lambda: self.tavern_dialogue(2),
                       bg="#3498db", fg="white", font=("Helvetica", 10),
                       wraplength=150)
        btn2.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
        
        btn3 = tk.Button(self.button_frame, text="'Qui êtes-vous ? Où suis-je ?'", 
                       command=lambda: self.tavern_dialogue(3),
                       bg="#3498db", fg="white", font=("Helvetica", 10),
                       wraplength=150)
        btn3.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
    
    def tavern_dialogue(self, choice):
        self.clear_text()
        self.clear_buttons()
        
        if choice == 1:
            self.print_text("- 'Non, je ne me souviens de rien,' répondez-vous en vous frottant la tête.")
            self.print_text("\n- 'Amnésie, hein ? C'est pas de chance,' dit le tavernier en essuyant un verre.")
            self.print_text("- 'Mais vous n'êtes pas le premier aventurier à avoir des problèmes près de la forêt ces derniers temps.'")
            self.print_text("- 'Il se passe des choses étranges depuis que la vieille tour au nord s'est mise à briller la nuit.'")
        elif choice == 2:
            self.print_text("- 'Vaguement... J'étais en mission,' dites-vous en essayant de rassembler vos souvenirs.")
            self.print_text("\n- 'Une mission ? Intéressant...' Le tavernier vous regarde avec plus d'attention.")
            self.print_text("- 'Beaucoup d'aventuriers viennent par ici ces temps-ci, attirés par les rumeurs de trésors dans les ruines.'")
            self.print_text("- 'Ou peut-être étiez-vous envoyé pour enquêter sur les disparitions ?'")
        else:
            self.print_text("- 'Qui êtes-vous ? Où suis-je ?' demandez-vous, confus.")
            self.print_text("\n- 'Du calme, l'ami !' Le tavernier lève les mains. 'Je suis Garen, propriétaire de l'Auberge du Sanglier Doré.'")
            self.print_text("- 'Vous êtes à Aubétoile, un petit village à la frontière du royaume. Pas grand-chose à voir ici, mais...'")
            self.print_text("- 'Nous avons nos problèmes. Des créatures sortent de la forêt la nuit, et des voyageurs disparaissent.'")
        
        self.print_text("\nAprès votre conversation avec le tavernier, vous décidez d'explorer le village.")
        self.print_text("Aubétoile est un petit village paisible, avec quelques maisons, une forge, un marché et un temple.")
        self.print_text("Vous remarquez que les villageois semblent nerveux, jetant régulièrement des regards vers la forêt au nord.")
        
        self.print_text("\nOù souhaitez-vous aller ?")
        
        # Boutons pour l'exploration du village
        btn1 = tk.Button(self.button_frame, text="Visiter la forge", 
                       command=self.visit_forge,
                       bg="#3498db", fg="white", font=("Helvetica", 12))
        btn1.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
        
        btn2 = tk.Button(self.button_frame, text="Aller au marché", 
                       command=self.visit_market,
                       bg="#3498db", fg="white", font=("Helvetica", 12))
        btn2.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
        
        btn3 = tk.Button(self.button_frame, text="Se rendre au temple", 
                       command=self.visit_temple,
                       bg="#3498db", fg="white", font=("Helvetica", 12))
        btn3.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
        
        btn4 = tk.Button(self.button_frame, text="Explorer les environs", 
                       command=self.explore_surroundings,
                       bg="#3498db", fg="white", font=("Helvetica", 12))
        btn4.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
    
    def visit_forge(self):
        self.clear_text()
        self.clear_buttons()
        
        self.print_text("Vous vous dirigez vers la forge du village. Le forgeron, un homme robuste aux bras musclés, frappe sur une épée incandescente.")
        self.print_text("En vous voyant approcher, il s'arrête et essuie son front couvert de sueur.")
        
        self.print_text("\n- 'Un nouvel aventurier, hein ?' dit-il. 'Si vous comptez explorer les environs, vous aurez besoin d'équipement.'")
        self.print_text("- 'Je peux vous vendre une épée pour 50 pièces d'or, ou une armure pour 75 pièces.'")
        
        # Boutons pour les achats
        if self.gold >= 50:
            sword_btn = tk.Button(self.button_frame, text="Acheter une épée (50 or)", 
                                command=lambda: self.buy_item("épée", 50, 20, 0),
                                bg="#e67e22", fg="white", font=("Helvetica", 12))
            sword_btn.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
        
        if self.gold >= 75:
            armor_btn = tk.Button(self.button_frame, text="Acheter une armure (75 or)", 
                                command=lambda: self.buy_item("armure", 75, 0, 20),
                                bg="#e67e22", fg="white", font=("Helvetica", 12))
            armor_btn.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
        
        back_btn = tk.Button(self.button_frame, text="Retourner au village", 
                           command=lambda: self.tavern_dialogue(1),  # Réutiliser la méthode pour afficher les options du village
                           bg="#7f8c8d", fg="white", font=("Helvetica", 12))
        back_btn.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
    
    def buy_item(self, item_name, cost, attack_bonus, defense_bonus):
        if self.gold >= cost:
            self.gold -= cost
            self.inventory.append(item_name)
            self.attack += attack_bonus
            self.defense += defense_bonus
            self.update_stats_display()
            
            self.print_text(f"\nVous avez acheté {item_name} pour {cost} pièces d'or.")
            if attack_bonus > 0:
                self.print_text(f"Votre attaque augmente de {attack_bonus} points.")
            if defense_bonus > 0:
                self.print_text(f"Votre défense augmente de {defense_bonus} points.")
        else:
            self.print_text("\nVous n'avez pas assez d'or pour cet achat.")
    
    def visit_market(self):
        self.clear_text()
        self.clear_buttons()
        
        self.print_text("Vous vous rendez au marché du village. Plusieurs étals proposent des produits frais, des herbes et des potions.")
        self.print_text("Une vieille femme vous fait signe d'approcher de son étal rempli de fioles colorées.")
        
        self.print_text("\n- 'Vous avez l'air d'un aventurier,' dit-elle avec un sourire édenté. 'J'ai exactement ce qu'il vous faut.'")
        self.print_text("- 'Des potions de soin, des élixirs de force, des antidotes... Tout ce dont un héros pourrait avoir besoin !'")
        
        # Boutons pour les achats
        if self.gold >= 30:
            potion_btn = tk.Button(self.button_frame, text="Acheter une potion de soin (30 or)", 
                                 command=lambda: self.buy_item("potion de soin", 30, 0, 0),
                                 bg="#e67e22", fg="white", font=("Helvetica", 12))
            potion_btn.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
        
        if self.gold >= 45:
            elixir_btn = tk.Button(self.button_frame, text="Acheter un élixir de force (45 or)", 
                                 command=lambda: self.buy_item("élixir de force", 45, 10, 0),
                                 bg="#e67e22", fg="white", font=("Helvetica", 12))
            elixir_btn.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
        
        back_btn = tk.Button(self.button_frame, text="Retourner au village", 
                           command=lambda: self.tavern_dialogue(1),
                           bg="#7f8c8d", fg="white", font=("Helvetica", 12))
        back_btn.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
    
    def visit_temple(self):
        self.clear_text()
        self.clear_buttons()
        
        self.print_text("Vous entrez dans le petit temple dédié au dieu de la lumière. L'intérieur est calme et paisible.")
        self.print_text("Un prêtre âgé s'approche de vous, son visage marqué par les années mais ses yeux brillants de sagesse.")
        
        self.print_text("\n- 'Bienvenue, voyageur,' dit-il doucement. 'Je sens que le destin vous a amené ici pour une raison.'")
        self.print_text("- 'Notre village est menacé par une ombre grandissante. Les créatures de la forêt deviennent agressives,'")
        self.print_text("- 'et une étrange lueur émane de la vieille tour au nord. Peut-être êtes-vous celui qui pourra nous aider ?'")
        
        self.print_text("\nLe prêtre vous propose de vous bénir avant votre départ.")
        
        # Boutons pour le temple
        blessing_btn = tk.Button(self.button_frame, text="Accepter la bénédiction", 
                               command=self.receive_blessing,
                               bg="#3498db", fg="white", font=("Helvetica", 12))
        blessing_btn.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
        
        back_btn = tk.Button(self.button_frame, text="Décliner et retourner au village", 
                           command=lambda: self.tavern_dialogue(1),
                           bg="#7f8c8d", fg="white", font=("Helvetica", 12))
        back_btn.pack(side=tk.LEFT, padx=10, pady=10, fill="x", expand=True)
    
    def receive_blessing(self):
        self.health += 50
        self.update_stats_display()
        
        self.print_text("\nLe prêtre pose ses mains sur votre tête et murmure une prière.")
        self.print_text("Vous vous sentez revigoré et prêt à affronter les dangers qui vous attendent.")
        self.print_text("Votre santé maximale augmente de 50 points.")
        
        # Bouton pour retourner au village
        back
if __name__ == "__main__":
    root = tk.Tk()
    app = DungeonHeroesGUI(root)
    root.mainloop()