from datetime import datetime

class Avis:
    def __init__(self, id_avis, contenu, auteur, lieu):
        self.id_avis = id_avis
        self.contenu = contenu
        self.auteur = auteur
        self.lieu = lieu
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
