from datetime import datetime

class Reminder:
    def __init__(self, name=None, dtime=None, amount=None) -> None:
        self.name = name
        self.dtime = dtime
        self.amount = amount
        
    def get_name(self) -> str:
        return self.name
    
    def get_datetime(self) -> datetime:
        return self.dtime
    
    def get_amount(self) -> int:
        return self.amount
    
    def set_name(self, name):
        self.name = name

    def set_datetime(self, dtime):
        self.dtime = dtime

    def set_amount(self, amount):
        self.amount = amount



