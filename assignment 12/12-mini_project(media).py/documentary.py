from media import Media

class Documentary(Media):
     def __init__(self,type,name,director,imdb_score,url,duration,actor,part,topic):
        Media.__init__(self,type,name,director,imdb_score,url,duration,actor)
        self.part = part
        self.topic = topic