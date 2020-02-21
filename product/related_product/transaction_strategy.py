from product.related_product.strategy import Strategy
from product.models import Product


class TransactionBaseStrategy(Strategy):
    def populated_related_product(self,product):
        return Product.objects.all()[:5]