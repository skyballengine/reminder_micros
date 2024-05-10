import datetime

class Reminder:
    def __init__(self, name, dtime) -> None:
        self.name = None
        self.dtime = None
        
    def get_name(self) -> str:
        return self.name
    
    def get_datetime(self) -> datetime:
        return self.dtime
    
    def set_name(self, name):
        self.name = name

    def set_datetime(self, dtime):
        self.dtime = dtime

        
