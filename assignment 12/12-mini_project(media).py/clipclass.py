from mediaclass import Media

class Clip(Media):
    def __init__(self, type, name, director, score, url, duration, casts, year, genre):
        super().__init__(type, name, director, score, url, duration, casts, year)
        self.genre=genre