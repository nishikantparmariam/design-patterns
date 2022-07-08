class IBird:

    def fly(self):
        raise NotImplementedError

class Eagle(IBird):

    def fly(self):
        print('I fly high')

class Sparrow(IBird):

    def fly(self):
        print('I fly slowly')


class NonBird(IBird):
    
    def fly(self):
        pass


def main():

    birds = [Eagle(), NonBird(), Sparrow()]

    for bird in birds:
        bird.fly()

main()