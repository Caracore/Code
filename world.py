from os import name
from typing import override

class World:
    def __init__(self):
        self.map = []
        self.current_room = None
        self.rooms = {} # Dictionnaire des salles, moins gros que map//
        self.name = name
    
    @override
    def __str__(self):
        return f"{self.name}"
    """def add_room(self, room):
        self.map.append(room)
    def set_start_room(self, room):
        self.current_room = room
    def get_current_room(self):
        return self.current_room
    def get_map(self):
        return self.map"""