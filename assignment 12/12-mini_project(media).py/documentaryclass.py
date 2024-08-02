from mediaclass import Media

class Documentary(Media):
    def __init__(self, type, name, director, score, url, duration, casts, year):
        super().__init__(type, name, director, score, url, duration, casts, year)