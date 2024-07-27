import pytube

class MEDIA():

    #properties
    def __init__(self , name , director , IMDB ,URL , duration , casts):
        self.name = name
        self.director = director
        self.IMDB_score = IMDB
        self.URL = URL
        self.duration = duration
        self.casts = casts

    #methods
    def show_info(self):
        print("Name:", self.name)
        print("Director", self.director)
        print("IMDB Score", self.IMDB)
        print("Duration", self.duration, "minutes")
        print("Casts: ", ', '.join([cast.name for cast in self.casts]))
    
    def download(self):
        link = self.url
        first_stream = pytube.YouTube (link) .streams.first ()
        first_stream.download(output_path = "./" , filename= self.name+".mp4" )


