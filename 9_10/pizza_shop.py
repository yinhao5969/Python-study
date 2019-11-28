from restaurant import Restaurant

class PizzaShop(Restaurant):
    def __init__(self, name, cuisine, flavor, servered=0):
        super(PizzaShop, self).__init__(name, cuisine, servered)
        self.flavor = flavor

    def show_flavor(self):
        print('best flavor is', self.flavor)

            
