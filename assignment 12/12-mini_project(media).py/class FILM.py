from MEDIA import MEDIA

class FILM(MEDIA):
    def __init__(self, name, director, IMDB ,URL, duration, casts, genre):
        super().__init__(name, director, IMDB ,URL, duration, casts)
        self.genre = genre