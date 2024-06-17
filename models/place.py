class Place:
    def init(self, place_id, name, location, host):
        self.place_id = place_id
        self.name = name
        self.location = location
        self.host = host
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)