class OrderStrategy:
    def process(self, order_id):
        raise NotImplementedError()

class PhysicalOrderStrategy(OrderStrategy):
    def process(self, order_id):
        return f"Shipping physical item #{order_id}"

class DigitalOrderStrategy(OrderStrategy):
    def process(self, order_id):
        return f"Sending download link for item #{order_id}"