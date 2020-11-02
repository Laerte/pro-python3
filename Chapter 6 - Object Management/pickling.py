import pickle


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        self.conversion = self.get_conversions()

    def __str__(self):
        return f'{self.amount:.2f} {self.currency}'

    def __repr__(self):
        return f'Money({self.amount}, {self.currency})'

    def __getstate__(self):
        return self.amount, self.currency

    def __setstate__(self, state):
        self.amount = state[0]
        self.currency = state[1]
        # When unpickling an object
        # Python doesn’t call __init__()
        self.conversion = self.get_conversions()

    def in_currency(self, currency):
        ratio = self.conversion[currency] / self.conversion[self.currency]
        return Money(self.amount * ratio, currency)

    def get_conversions(self):
        return {'USD': 1, 'CAD': .95}


us_dollar = Money(250, 'USD')
print(repr(us_dollar))
print(repr(us_dollar.in_currency('CAD')))

pickled = pickle.dumps(us_dollar)

us_dollar = pickle.loads(pickled)
print(repr(us_dollar.in_currency('CAD')))

