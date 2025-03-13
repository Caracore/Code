class Voiture:
    def __init__(self, name, description, marque, vitesse_max, roues):
        self.name = name
        self.description = description
        self.marque = marque
        self.vitesse_max = vitesse_max
        self.roues = roues
    def accélérer(self, vitesse, vitesse_max):
        if self.vitesse == 0:
            self.vitesse += 1
        if vitesse == vitesse_max:
            self.vitesse = vitesse_max
        if vitesse_max:
            self.vitesse += 0
        else:
            self.vitesse += 1
    def ralentir(self, vitesse, vitesse_max):
        if self.vitesse == 0:
            self.vitesse = 0
        if vitesse <= vitesse_max:
            self.vitesse -= 1
        else:
            self.vitesse += 0
    def __str__(self):
        return f"{self.name} ({self.description})\nMarque: {self.marque}\nVitesse max: {self.vitesse_max} km/h\nRoues: {self.roues}"
    
       