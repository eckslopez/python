from annual import Annual
from datetime import datetime

class AnnualCorporate(Annual):

    @property
    def price(self):
        return super().price * .8
