class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  # Attribut privé
        self.__largeur = largeur  # Attribut privé

    # C'est la mthode pour calculer le périmètre
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    # C'est la méthode pour calculer la surface
    def surface(self):
        return self.__longueur * self.__largeur

    # C'est l'assesseur pour longueur
    def get_longueur(self):
        return self.__longueur

    # Mutateur pour longueur
    def set_longueur(self, longueur):
        self.__longueur = longueur

    # Assesseur pour largeur
    def get_largeur(self):
        return self.__largeur

    # Mutateur pour largeur
    def set_largeur(self, largeur):
        self.__largeur = largeur

# C'est la classe Parallelepipede héritée de Rectangle
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)  # J'appel le constructeur de la classe
        self.__hauteur = hauteur  # Attribut privé

    # Méthode pour calculer le volume
    def volume(self):
        return self.surface() * self.__hauteur 

    # Assesseur pour hauteur
    def get_hauteur(self):
        return self.__hauteur

    # Mutateur pour hauteur
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

# Instanciation de la classe Rectangle
rectangle = Rectangle(5, 3)

# J'affiche le périmètre et de la surface du rectangle
print(f"Périmètre du rectangle : {rectangle.perimetre()}")  # Périmètre = 2 * (longueur + largeur)
print(f"Surface du rectangle : {rectangle.surface()}")  # Surface = longueur * largeur

# Je modifie lesz dimensions du rectangle avec les mutateurs
rectangle.set_longueur(7)
rectangle.set_largeur(4)

# Affichage après modification
print(f"Nouvelle surface du rectangle : {rectangle.surface()}")
print(f"Nouveau périmètre du rectangle : {rectangle.perimetre()}")

# Instanciation de la classe Parallelepipede
parallelepipede = Parallelepipede(7, 4, 10)

# Affichage du volume du parallélépipède
print(f"Volume du parallélépipède : {parallelepipede.volume()}")  # Volume = surface * hauteur