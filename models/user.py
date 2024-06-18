# modèle/utilisateur.py

from datetime import datetime

class Utilisateur:
    emails_utilisateurs = set()

    def __init__(self, id_utilisateur, email, nom):
        if email in Utilisateur.emails_utilisateurs:
            raise ValueError("Cet email est déjà utilisé.")
        Utilisateur.emails_utilisateurs.add(email)
        
        self.id_utilisateur = id_utilisateur
        self.email = email
        self.nom = nom
        self.lieux = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def ajouter_lieu(self, lieu):
        if lieu not in self.lieux:
            self.lieux.append(lieu)
            lieu.hôte = self  # relation lieu hôte
        self.updated_at = datetime.now()

    def mettre_a_jour(self, nom=None):
        if nom:
            self.nom = nom
        self.updated_at = datetime.now()
