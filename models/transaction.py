from datetime import datetime, date 


class Transaction:

    def __init__(self, input_amount, tag, merchant, date, id = None):
        self.amount = input_amount
        self.tag = tag
        self.merchant = merchant
        self.date = date
        self.id = id