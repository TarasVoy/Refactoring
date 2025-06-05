class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.orders = []

    def register(self):
        return f"User {self.username} registered."

    def login(self):
        return f"User {self.username} logged in."

    def view_orders(self):
        return self.orders

    def add_order(self, order):
        self.orders.append(order)