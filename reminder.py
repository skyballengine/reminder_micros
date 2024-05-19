from datetime import datetime, date

class Reminder:
    def __init__(self, name=None, date=None, amount=None) -> None:
        self.name = name
        self.date = date
        self.amount = amount
        
    def get_name(self) -> str:
        return self.name
    
    def get_date(self) -> date:
        return self.date
    
    def get_amount(self) -> int:
        return self.amount
    
    def set_name(self, name):
        self.name = name

    def set_date(self, date):
        self.date = date

    def set_amount(self, amount):
        self.amount = amount



