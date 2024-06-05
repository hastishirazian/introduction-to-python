class time:

    #properties
    def __init__(self,hour,minute,second):
        #properties
        self.hour = h
        self.minute = m
        self.second = s


    #methods
    def set_time(self,hour,minute,second):
        ...
    
    def hourTOminute(self,hour,minute):
        ...
    def minutteTOsecond(self,minute,second):
        ...
    def hourTOsecond(self,hour,second):
        ...

time1 = time(14,23,17)
print(time1)