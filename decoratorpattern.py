class IBeverage:

    def cost(self):
        raise NotImplemented

class Mocha(IBeverage):

    def cost(self):
        return 5


class Espresso(IBeverage):

    def cost(self):
        return 8


class IBeverageDecorator(IBeverage):

    def cost(self):
        raise NotImplemented


class SoyaAddon(IBeverageDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 4

class MilkAddon(IBeverageDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 8


class CaramelAddon(IBeverageDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 1


#########################################


def main():

    beverage1 = Mocha()
    beverage2 = CaramelAddon(MilkAddon(SoyaAddon(Espresso())))
    beverage3 = CaramelAddon(MilkAddon(Espresso()))
    beverage4 = SoyaAddon(CaramelAddon(Mocha()))

    print(beverage1.cost())
    print(beverage2.cost())
    print(beverage3.cost())
    print(beverage4.cost())

main()