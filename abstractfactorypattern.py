class Button:
    pass

class DarkThemeButton(Button):
    pass

class LightThemeButton(Button):
    pass

class GreyThemeButton(Button):
    pass


class Background:
    pass

class DarkThemeBackground(Background):
    pass

class LightThemeBackground(Background):
    pass

class GreyThemeBackground(Background):
    pass

class UIFactory:

    def createButton(self):
        raise NotImplemented

    def createBackground(self):
        raise NotImplemented


class DarkUIFactory(UIFactory):

    def createBackground(self):
        return GreyThemeBackground()

    def createButton(self):
        return DarkThemeButton()


class MildUIFactory(UIFactory):

    def createBackground(self):
        return LightThemeBackground()

    def createButton(self):
        return LightThemeButton()


def main():

    darkUIFactory = DarkUIFactory()
    mildUIFactory = MildUIFactory()

    print(darkUIFactory.createButton(), mildUIFactory.createButton())
    print(darkUIFactory.createBackground(), mildUIFactory.createBackground())

main()