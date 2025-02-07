# Je crée d'abord la classe Personne avec un attribut d'instance age initialisé à 14 par défaut. La méthode afficherAge affiche l'âge de la personne, la méthode bonjour affiche un message de salutation et la méthode modifierAge modifie l'âge de la personne. Ensuite, je crée la classe Eleve qui hérite de la classe Personne. La classe Eleve a une méthode allerEnCours qui affiche un message indiquant que l'élève va en cours, et une méthode afficherAge qui affiche l'âge de l'élève dans un format spécifique. Enfin, je crée la classe Professeur avec un attribut privé matiereEnseignee et une méthode enseigner qui affiche un message indiquant que le cours va commencer. Je crée une instance de la classe Personne et de la classe Eleve, et j'appelle les méthodes afficherAge pour vérifier que les classes fonctionnent correctement.
class Personne:
    def __init__(self, age=14):
        self.age = age 

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
    def __init__(self, matiereEnseignee, age=40):
        self.__matiereEnseignee = matiereEnseignee 
        self.age = age  

    def enseigner(self):
        """Affiche un message indiquant que le cours va commencer."""
        print("Le cours va commencer.")

    def bonjour(self):
        """Le professeur dit bonjour."""
        print("Bonjour")

eleve = Eleve()

eleve.bonjour()  
eleve.allerEnCours()  

eleve.modifierAge(15)

eleve.afficherAge() 

professeur = Professeur(matiereEnseignee="Mathématiques")

professeur.bonjour()  
professeur.enseigner() 