from datetime import datetime

class Lieu:
    def __init__(self, id_lieu, nom, hôte, latitude=None, longitude=None, prix_par_nuit=None, max_invites=None):
        if hôte is None:
            raise ValueError("Un lieu doit avoir un hôte.")
        
        self.id_lieu = id_lieu
        self.nom = nom
        self.hôte = hôte
        self.avis = []
        self.amenities = []
        self.latitude = latitude
        self.longitude = longitude
        self.prix_par_nuit = prix_par_nuit
        self.max_invites = max_invites
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def ajouter_avis(self, avis):
        if avis not in self.avis:
            self.avis.append(avis)
        self.updated_at = datetime.now()

    def ajouter_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)
        self.updated_at = datetime.now()
