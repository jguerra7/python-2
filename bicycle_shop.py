class Bicycle:
    def __init__(self, m, w, c):
        self.model = m
        self.weight = w
        self.cost = c

    def set_model(self, m):
        self.model = m

    def set_weight(self, w):
        self.weight = w

    def set_cost(self, c):
        self.cost = c


class Customer:
    def __init__(self, n, b):
        self.name = n
        self.budget = b

    def set_name(self, n):
        self.name = n

    def set_budget(self, b):
        self.budget = b

    def buy_bike(self, c):
        self.budget -= c


class BikeShop:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def set_name(self, value):
        self.name = value

    def sell_bike(self, bike):
        self.inventory.remove(bike)

    def add_bike(self, model, weight, cost):
        self.inventory.append(Bicycle(model, weight, cost))

    def print_inventory(self):
        print(self.inventory)


bike_shop = BikeShop("Ninja Stole My Bike")
bike_shop.add_bike("Huffy", "25", "125")

bike_shop.print_inventory()
