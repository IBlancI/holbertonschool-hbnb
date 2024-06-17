from .user.py import User

class Host(User):
    def init(self, user_id, email, name, host_id):
        super().init(user_id, email, name)
        self.host_id = host_id
        self.places = []

    def add_place(self, place):
        self.places.append(place)