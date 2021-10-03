class Transaction:

    def __init__(self, input_amount, tag, merchant, id = None):
        self.amount = input_amount
        self.tag = tag
        self.merchant = merchant
        self.id = id