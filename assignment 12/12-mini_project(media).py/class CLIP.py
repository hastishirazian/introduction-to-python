from MEDIA import MEDIA

class Clip(MEDIA):
    def __init__(self, name, director, IMDB, URL, duration, casts, category):
        super().__init__(self, name, director, IMDB, URL, duration, casts)
        self.category = category