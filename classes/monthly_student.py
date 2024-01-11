from monthly import Monthly
from datetime import datetime

class MonthlyStudent(Monthly):
    
    def price(self):
        return super().price * .9
