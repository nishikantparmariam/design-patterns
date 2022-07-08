class AnimalFactory:

    def createAnimal(self):
        raise NotImplemented


class Animal:
    pass

class Duck(Animal):
    pass

class Tiger(Animal):
    pass

class Lion(Animal):
    pass


class RandomFactory(AnimalFactory):

    def createAnimal(self):
        return Tiger()


class NonUniformFactory(AnimalFactory):

    def createAnimal(self):
        return Duck()

def main():

    randomFactory = RandomFactory()
    nonUniformFactory = NonUniformFactory()

    print(randomFactory.createAnimal(), nonUniformFactory.createAnimal())

main()