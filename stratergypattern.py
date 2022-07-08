class IFlyBehavior:

    def fly(self):
        raise NotImplementedError


class IQuackBehavior:

    def quack(self):
        raise NotImplementedError


class JetFlyBehavior(IFlyBehavior):

    def fly(self):
        print('Flying super fast with jet!')

class SimpleFlyBehavior(IFlyBehavior):

    def fly(self):
        print('Flying with wings!')


class MegaQuackBehavior(IQuackBehavior):

    def quack(self):
        print('Quacking megaly')


class Duck:

    def __init__(self, flyBehavior, quackBehavior):
        self.flyBehavior = flyBehavior
        self.quackBehavior = quackBehavior


    def fly(self):
        self.flyBehavior.fly()

    def quack(self):
        self.quackBehavior.quack()


def main():

    wildDuck = Duck(JetFlyBehavior(), MegaQuackBehavior())
    cloudDuck = Duck(SimpleFlyBehavior(), MegaQuackBehavior())

    wildDuck.fly()
    wildDuck.quack()
    cloudDuck.fly()
    cloudDuck.quack()

main()