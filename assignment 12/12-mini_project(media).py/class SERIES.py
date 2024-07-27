from MEDIA import MEDIA

class SERIES(MEDIA):
    def __init__(self, name, director, IMDB, URL, duration, casts, episodes):
        super().__init__(name, director, IMDB, URL, duration, casts)
        self.episodes = episodes

    def show_info(self):
        super().show_info()
        print("Episodes:", self.episodes)