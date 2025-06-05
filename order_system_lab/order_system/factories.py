from .strategies import PhysicalOrderStrategy, DigitalOrderStrategy

class OrderFactory:
    @staticmethod
    def create_order(order_type):
        if order_type == "physical":
            return PhysicalOrderStrategy()
        elif order_type == "digital":
            return DigitalOrderStrategy()
        else:
            raise ValueError("Unknown order type")