class ICommand:

    def execute(self):
        raise NotImplementedError
    
    def unexecute(self):
        raise NotImplementedError


class Light:

    def on(self):
        print('Turned light on')

    def off(self):
        print('Turned light off')


class Car:

    def startEngine(self):
        print('Ignition on')

    def stopEngine(self):
        print('Ignition off')

class CarCommand(ICommand):

    def __init__(self, car):
        self.car = car

    def execute(self):
        self.car.startEngine()

    def unexecute(self):
        self.car.stopEngine()


class LightCommand(ICommand):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def unexecute(self):
        self.light.off()


class Invoker:

    def __init__(self, lightCommand, carCommand):
        self.lightCommand = lightCommand
        self.carCommand = carCommand

    def do(self):
        self.lightCommand.execute()
        self.carCommand.execute()

    def undo(self):
        self.carCommand.unexecute()
        self.lightCommand.unexecute()

############################################


def main():

    phillipsRemote = Invoker(LightCommand(Light()), CarCommand(Car()))
    dellRemote = Invoker(LightCommand(Light()), CarCommand(Car()))

    phillipsRemote.do()
    dellRemote.do()
    dellRemote.undo()
    phillipsRemote.undo()

main()