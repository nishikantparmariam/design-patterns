class IView:

    def show(self):
        raise NotImplemented


class IMediaResource:

    def getHTML(self):
        raise NotImplemented


class Car:

    def getEngineName(self):
        return ' V4 - Diesel '

class User:

    def getFullName(self):
        return ' Harish Tank '


class UserMediaResource(IMediaResource):

    def __init__(self, user):
        self.user = user

    def getHTML(self):
        return self.user.getFullName()

class CarMediaResource(IMediaResource):

    def __init__(self, car):
        self.car = car

    def getHTML(self):
        return self.car.getEngineName()


class LongFormView(IView):

    def __init__(self, mediaResource):
        self.mediaResource = mediaResource

    def show(self):
        return 'Hi! - ' + self.mediaResource.getHTML()        

class ShortFormView(IView):

    def __init__(self, mediaResource):
        self.mediaResource = mediaResource

    def show(self):
        return self.mediaResource.getHTML()        

class CardFormView(IView):

    def __init__(self, mediaResource):
        self.mediaResource = mediaResource

    def show(self):
        return self.mediaResource.getHTML() + ' - Thanks!'


def main():

    view1 = LongFormView(CarMediaResource(Car()))
    view2 = LongFormView(UserMediaResource(User()))
    view3 = CardFormView(CarMediaResource(Car()))
    view4 = CardFormView(UserMediaResource(User()))
    view5 = ShortFormView(CarMediaResource(Car()))
    view6 = ShortFormView(UserMediaResource(User()))


    print(view1.show())
    print(view2.show())
    print(view3.show())
    print(view4.show())
    print(view5.show())
    print(view6.show())

main()

