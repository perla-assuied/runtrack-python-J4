class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        """Méthode pour afficher les informations du véhicule"""
        print(f"Marque : {self.marque}, Modèle : {self.modele}, Année : {self.annee}, Prix : {self.prix}€")
    
    def demarrer(self):
        """Méthode de démarrage du véhicule"""
        print("Attention, je roule.")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        """Méthode qui affiche les informations générales du véhicule et le nombre de portes"""
        super().informationsVehicule()
        print(f"Nombre de portes : {self.portes}")
    
    def demarrer(self):
        """Méthode de démarrage de la voiture"""
        print("Vroom vroom, la voiture démarre!")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, modele, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        """Méthode qui affiche toutes les informations de la moto"""
        super().informationsVehicule()
        print(f"Nombre de roues : {self.roue}")
    
    def demarrer(self):
        """Méthode de démarrage de la moto"""
        print("Vroom, la moto rugit!")

# Je crée un objet Voiture
voiture = Voiture("Peugeot", "208", 2020, 15000)
voiture.informationsVehicule()  # infos de la voiture 
voiture.demarrer()  # Démarrer la voiture

# Je crée un objet Moto
moto = Moto("Yamaha", "MT-07", 2021, 8000)
moto.informationsVehicule()  # infos de la moto 
moto.demarrer()  # Démarrer la moto