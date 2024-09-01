from media import Media

class Series(Media):
    def __init__(self,type,name,director,imdb_score,url,duration,actor,part,num_episodes):
        Media.__init__(self,type,name,director,imdb_score,url,duration,actor)
        self.part = part
        self.num_episodes = num_episodes