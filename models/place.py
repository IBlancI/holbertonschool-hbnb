# modèle/lieu.py

class Lieu:
    def __init__(self, id_lieu, nom, hôte):
        if hôte is None:
            raise ValueError("Un lieu doit avoir un hôte.")
        
        self.id_lieu = id_lieu
        self.nom = nom
        self.hôte = hôte
        self.avis = []

    def ajouter_avis(self, avis):
        if avis not in self.avis:
            self.avis.append(avis)
