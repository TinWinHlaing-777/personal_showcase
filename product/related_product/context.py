

class Context():
    def __init__(self,strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self,strategy):
        self._strategy = strategy

    def get_related_product(self,product):
        return self._strategy.populate_related_product(product)

