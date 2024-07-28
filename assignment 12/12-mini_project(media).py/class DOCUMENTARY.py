from MEDIA import MEDIA

class DOCUMENTARY(MEDIA):
    def __init__(self, name, director, IMDB, URL, duration, casts, subject):
        super().__init__(name, director, IMDB, URL, duration, casts)
        self.subject = subject