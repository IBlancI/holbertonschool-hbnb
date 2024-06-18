from datetime import datetime

class Amenity:
    def __init__(self, id_amenity, nom):
        self.id_amenity = id_amenity
        self.nom = nom
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
