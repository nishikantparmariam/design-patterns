class IIterable:

    def getIterator(self):
        raise NotImplemented


class IIterotor:

    def hasNext(self):
        raise NotImplemented

    def moveToNext(self):
        raise NotImplemented

    def getCurr(self):
        raise NotImplemented


class HouseIterator(IIterotor):

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def hasNext(self):
        return self.index < len(self.iterable.store)

    def moveToNext(self):
        self.index = self.index + 1

    def getCurr(self):
        return self.iterable.store[self.index]


class House(IIterable):

    def __init__(self):
        self.store = [13,34,78,7]

    def getIterator(self):
        return HouseIterator(self)



def main():

    house = House()
    houseIterator = house.getIterator()

    while houseIterator.hasNext():

        print(houseIterator.getCurr())
        houseIterator.moveToNext()

main()