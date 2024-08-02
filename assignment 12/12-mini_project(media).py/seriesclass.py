from mediaclass import Media

class Series(Media):
    def __init__(self, type, name, director, score, url, duration, casts, year, episode):
        super().__init__(type, name, director, score, url, duration, casts, year)
        self.episodnumber = episode