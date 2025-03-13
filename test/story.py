import personnage_init , world , personnage, item_init, menu

"""def story():
    storyline = []
    pass
    return storyline
"""
class Story():
    def __init__(self):
        self.name = ""
        self.storyline = []
        self.quest = []
        self.location = []
        self.item = []
        self.mode = []
        self.scenario = []
        self.variable = []
    
class Quest(Story):
    def __init__(self, name, storyline, quest, location, item, scenario, variable, mode):
        super().__init__()
    def quest_create(self):
        if mode == "combat":
            pass
        elif mode == "scenario":
            pass
        else:
            pass