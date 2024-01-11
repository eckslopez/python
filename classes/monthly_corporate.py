from monthly import Monthly
from datetime import datetime

class MonthlyCorporate(Monthly):

    def price(self):
        return super().price * .8