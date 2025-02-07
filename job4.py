# Classe Forme
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

# Création d'1 objet Rectangle
rectangle = Rectangle(5, 3)

# J'affiche l'aire du rectangle
print(f"L'aire du rectangle est : {rectangle.aire()}")  # Devrait afficher 15 5 * 3
