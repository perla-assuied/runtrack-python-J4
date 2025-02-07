import math
class Forme:
    def aire(self):
        """Méthode qui renvoie 0, car ce n'est pas défini pour une forme générale."""
        return 0

# Classe Rectangle qui hérite de Forme
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    # Surcharge de la méthode aire pour calculer l'aire du rectangle
    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius  # Attribut pour le rayon du cercle

    # Surcharge de la méthode aire pour calculer l'aire du cercle
    def aire(self):
        return math.pi * (self.radius ** 2)  # Aire du cercle : π * r²
    
# Je crez un objet Rectangle
rectangle = Rectangle(5, 3)

# Je crée u²n objet Cercle
cercle = Cercle(4)

# Affichage de l'aire du rectangle
print(f"L'aire du rectangle est : {rectangle.aire()}")  # 5 * 3 = 15

# Affichage de l'aire du cercle
print(f"L'aire du cercle est : {cercle.aire()}")  # π * 4² ≈ 50.265