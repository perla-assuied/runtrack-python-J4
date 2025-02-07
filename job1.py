# Jeu de tests pour les classes Personne et Eleve, et la classe Professeur, définies dans le fichier.j'initialise les classes Personne et Eleve, et la classe Professeur, je crée une instance de chaque classe et j'appelle les méthodes de chaque instance pour vérifier que les classes fonctionnent correctement.
class Personne:
    def __init__(self, age=14):
        self.age = age  # Attribut avec valeur par défaut de 14

    def afficherAge(self):
        """Affiche l'âge de la personne."""
        print(f"J'ai {self.age} ans.")

    def bonjour(self):
        """Affiche un message de salutation."""
        print("Hello")

    def modifierAge(self, nouvel_age):
        """Modifie l'âge de la personne."""
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        """Affiche un message indiquant que l'élève va en cours."""
        print("Je vais en cours.")
        
    def afficherAge(self):
        """Affiche l'âge de l'élève dans un format spécifique."""
        print(f"J'ai {self.age} ans.")
class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee  # Attribut privé

    def enseigner(self):
        """Affiche un message indiquant que le cours va commencer."""
        print("Le cours va commencer.")

personne = Personne()
personne.afficherAge()  # Affiche l'âge par défaut (14)

eleve = Eleve()
eleve.afficherAge()  # Affiche l'âge de l'élève (par défaut 14)