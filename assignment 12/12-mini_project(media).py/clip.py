from media import Media

class Clip(Media):
   def __init__(self,type,name,director,imdb_score,url,duration,actor,category):
       Media.__init__(self,type,name,director,imdb_score,url,duration,actor)
       self.category = category