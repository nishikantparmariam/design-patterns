class IObservable:

    def add(self, observer):
        raise NotImplemented

    def remove(self, observer):
        raise NotImplemented

    def notify(self):
        raise NotImplemented

    def getState(self):
        raise NotImplemented



class IObserver:

    def update(self):
        raise NotImplemented


########################################


class WeatherStation(IObservable):

    def __init__(self):
        self.observers = []

    def add(self, observer):
        self.observers.append(observer)

    def remove(self, observer):
        self.observers.remove(observer)

    def getState(self):
        return 8

    def notify(self):
        for observer in self.observers:
            observer.update()

#################################


class PhoneDisplay(IObserver):

    def __init__(self, observable):
        self.observable = observable

    def update(self):
        print('Updating to from Phone -', self.observable.getState())


class LCDDisplay(IObserver):

    def __init__(self, observable):
        self.observable = observable

    def update(self):
        print('Updating to from LCD -', self.observable.getState())


##################


def main():

    weatherStation = WeatherStation()
    
    phone1 = PhoneDisplay(weatherStation)
    phone2 = PhoneDisplay(weatherStation)
    phone3 = PhoneDisplay(weatherStation)

    lcd1 = LCDDisplay(weatherStation)
    lcd2 = LCDDisplay(weatherStation)
    lcd3 = LCDDisplay(weatherStation)

    weatherStation.add(phone2)
    weatherStation.add(lcd3)
    weatherStation.add(lcd1)
    weatherStation.add(phone1)    
    weatherStation.add(lcd2)    
    weatherStation.add(phone3)

    weatherStation.notify()


main()