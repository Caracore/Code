#!/usr/bin/env python

# Importation des classes nécessaires depuis __init__complet.py
from __init__complet import Personnage, Item, PotionSoin, Arme, Armure, Quest, World, Room

# Importation des modules Panda3D
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *
from panda3d.core import *

import os
import sys
import random
import time

# Configuration de base pour Panda3D
loadPrcFileData("", """
    window-title Aventure RPG 3D
    win-size 1280 720
    cursor-hidden 0
    show-frame-rate-meter 1
    sync-video 0
    model-path models
    texture-path textures
""")

class GameApp(ShowBase):
    """
    Classe principale du jeu 3D basée sur Panda3D.
    """
    
    def __init__(self):
        """
        Initialise l'application du jeu.
        """
        ShowBase.__init__(self)
        
        # Désactiver la caméra par défaut de Panda3D
        self.disableMouse()
        
        # Initialisation des variables du jeu
        self.joueur = None
        self.monde = None
        self.salle_courante = None
        self.ennemis = []
        self.quetes_disponibles = []
        self.quetes_actives = []
        self.quetes_terminees = []
        self.running = True
        
        # État du jeu
        self.game_state = "MENU"  # MENU, GAME, COMBAT, INVENTORY, QUESTS, TRAVEL
        
        # Création du skybox
        self.setup_skybox()
        
        # Création du terrain
        self.setup_terrain()
        
        # Création de l'éclairage
        self.setup_lighting()
        
        # Création de l'interface utilisateur
        self.setup_ui()
        
        # Création de la caméra
        self.setup_camera()
        
        # Ajouter les tâches
        self.taskMgr.add(self.update, "update")
        
        # Ajouter les contrôles
        self.setup_controls()
        
        # Démarrer le menu principal
        self.show_main_menu()
    
    def setup_skybox(self):
        """
        Configure le skybox pour le jeu.
        """
        # Créer un skybox simple de couleur bleue
        self.skybox = self.loader.loadModel("models/box")
        self.skybox.setScale(500)
        self.skybox.setPos(0, 0, 0)
        self.skybox.reparentTo(self.render)
        
        # Appliquer une texture de ciel
        skybox_texture = self.loader.loadTexture("textures/sky.jpg")
        self.skybox.setTexture(skybox_texture, 1)
    
    def setup_terrain(self):
        """
        Configure le terrain pour le jeu.
        """
        # Créer un terrain simple
        self.terrain = self.loader.loadModel("models/plane")
        self.terrain.setScale(100, 100, 1)
        self.terrain.setPos(0, 0, -1)
        self.terrain.reparentTo(self.render)
        
        # Appliquer une texture de terrain
        terrain_texture = self.loader.loadTexture("textures/grass.jpg")
        self.terrain.setTexture(terrain_texture, 1)
    
    def setup_lighting(self):
        """
        Configure l'éclairage pour le jeu.
        """
        # Lumière ambiante
        ambient_light = AmbientLight("ambient_light")
        ambient_light.setColor((0.3, 0.3, 0.3, 1))
        ambient_light_np = self.render.attachNewNode(ambient_light)
        self.render.setLight(ambient_light_np)
        
        # Lumière directionnelle (soleil)
        directional_light = DirectionalLight("directional_light")
        directional_light.setColor((0.8, 0.8, 0.8, 1))
        directional_light_np = self.render.attachNewNode(directional_light)
        directional_light_np.setHpr(45, -45, 0)
        self.render.setLight(directional_light_np)
    
    def setup_ui(self):
        """
        Configure l'interface utilisateur pour le jeu.
        """
        # Créer un cadre pour les informations du joueur
        self.player_info_frame = DirectFrame(
            frameColor=(0, 0, 0, 0.7),
            frameSize=(-0.3, 0.3, -0.1, 0.1),
            pos=(-1, 0, 0.9)
        )
        
        # Texte pour les informations du joueur
        self.player_info_text = OnscreenText(
            text="",
            pos=(-0.95, 0.85),
            scale=0.05,
            fg=(1, 1, 1, 1),
            align=TextNode.ALeft,
            mayChange=True
        )
        
        # Créer un cadre pour les messages
        self.message_frame = DirectFrame(
            frameColor=(0, 0, 0, 0.7),
            frameSize=(-0.5, 0.5, -0.1, 0.1),
            pos=(0, 0, -0.8)
        )
        
        # Texte pour les messages
        self.message_text = OnscreenText(
            text="Bienvenue dans l'Aventure RPG 3D!",
            pos=(0, -0.85),
            scale=0.05,
            fg=(1, 1, 1, 1),
            align=TextNode.ACenter,
            mayChange=True
        )
        
        # Masquer les éléments UI au démarrage
        self.player_info_frame.hide()
        self.message_frame.hide()
    
    def setup_camera(self):
        """
        Configure la caméra pour le jeu.
        """
        # Positionner la caméra
        self.camera.setPos(0, -10, 5)
        self.camera.lookAt(0, 0, 0)
    
    def setup_controls(self):
        """
        Configure les contrôles du jeu.
        """
        # Définir les contrôles clavier
        self.accept("escape", self.show_main_menu)
        self.accept("i", self.show_inventory)
        self.accept("q", self.show_quests)
        self.accept("m", self.show_map)
        
        # Contrôles de mouvement
        self.accept("w", self.set_key, ["forward", True])
        self.accept("w-up", self.set_key, ["forward", False])
        self.accept("s", self.set_key, ["backward", True])
        self.accept("s-up", self.set_key, ["backward", False])
        self.accept("a", self.set_key, ["left", True])
        self.accept("a-up", self.set_key, ["left", False])
        self.accept("d", self.set_key, ["right", True])
        self.accept("d-up", self.set_key, ["right", False])
        
        # Initialiser les touches
        self.keys = {
            "forward": False,
            "backward": False,
            "left": False,
            "right": False
        }
    
    def set_key(self, key, value):
        """
        Définit l'état d'une touche.
        
        Args:
            key (str): La touche à définir
            value (bool): L'état de la touche
        """
        self.keys[key] = value
    
    def update(self, task):
        """
        Fonction de mise à jour appelée à chaque frame.
        
        Args:
            task: La tâche Panda3D
            
        Returns:
            Task.cont: Pour continuer la tâche
        """
        # Mettre à jour le jeu en fonction de l'état
        if self.game_state == "GAME":
            # Mettre à jour le mouvement du joueur
            self.update_player_movement()
            
            # Mettre à jour les informations du joueur
            if self.joueur:
                self.player_info_text.setText(
                    f"Nom: {self.joueur.nom}\n"
                    f"Vie: {self.joueur.vie}/{self.joueur.max_vie}\n"
                    f"Force: {self.joueur.force}\n"
                    f"Défense: {self.joueur.defense}"
                )
        
        return Task.cont
    
    def update_player_movement(self):
        """
        Met à jour le mouvement du joueur en fonction des touches pressées.
        """
        if not hasattr(self, "player_model"):
            return
        
        # Vitesse de déplacement
        speed = 0.1
        
        # Calculer le déplacement
        x_movement = 0
        y_movement = 0
        
        if self.keys["forward"]:
            y_movement += speed
        if self.keys["backward"]:
            y_movement -= speed
        if self.keys["left"]:
            x_movement -= speed
        if self.keys["right"]:
            x_movement += speed
        
        # Appliquer le déplacement
        self.player_model.setPos(
            self.player_model.getX() + x_movement,
            self.player_model.getY() + y_movement,
            self.player_model.getZ()
        )
        
        # Mettre à jour la caméra pour suivre le joueur
        self.camera.setPos(
            self.player_model.getX(),
            self.player_model.getY() - 10,
            self.player_model.getZ() + 5
        )
        self.camera.lookAt(self.player_model)
# a voir si la partie du bas marche ?

    def start_combat(self, enemy):
        # Passer en mode combat
        self.game_state = "COMBAT"
        
        # Afficher l'interface de combat
        self.show_combat_ui(enemy)
        
        # Positionner l'ennemi face au joueur
        enemy_model = self.enemy_models[enemy.nom]
        enemy_model.setPos(
            self.player_model.getX() + 3,
            self.player_model.getY(),
            self.player_model.getZ()
        )
        enemy_model.lookAt(self.player_model)
        
        # Désactiver les contrôles de mouvement
        self.disable_movement_controls()

    def player_attack(self, enemy):
        # Jouer l'animation d'attaque
        self.player_model.play("attack")
        
        # Calculer les dégâts
        degats = self.joueur.attaquer(enemy)
        
        # Afficher les dégâts
        self.show_damage_text(enemy, degats)
        
        # Vérifier si l'ennemi est vaincu
        if enemy.vie <= 0:
            self.end_combat(victory=True)
        else:
            # L'ennemi riposte après un court délai
            self.taskMgr.doMethodLater(1.0, self.enemy_attack, "enemy_attack", extraArgs=[enemy])

    def enemy_attack(self, enemy):
        # Jouer l'animation d'attaque
        self.player_model.play("attack")
        
        # Calculer les dégâts
        degats = self.joueur.attaquer(enemy)
        
        # Afficher les dégâts
        self.show_damage_text(enemy, degats)
        
        # Vérifier si l'ennemi est vaincu
        if enemy.vie <= 0:
            self.end_combat(victory=True)
        else:
            # L'ennemi riposte après un court délai
            self.taskMgr.doMethodLater(1.0, self.enemy_attack, "enemy_attack", extraArgs=[enemy])