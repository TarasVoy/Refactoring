from .factories import OrderFactory

class OrderProcessor:
    def __init__(self, order_type):
        self.strategy = OrderFactory.create_order(order_type)

    def process_order(self, order_id):
        return self.strategy.process(order_id)