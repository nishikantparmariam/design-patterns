class SingleTon:

    __singleTonObj = None

    @classmethod
    def getInstance(cls):

        if not cls.__singleTonObj:
            cls.__singleTonObj = SingleTon()

        return cls.__singleTonObj


    def __init__(self):
        if not self.__class__.__singleTonObj:
            self.__class__.__singleTonObj = self
        else:
            raise Exception('Cannot instantiate SingleTon twice')


def main():


    obj1 = SingleTon()
    print(id(obj1))

    obj2 = SingleTon.getInstance()
    print(id(obj2))

    obj2 = SingleTon.getInstance()
    print(id(obj2))

    obj3 = SingleTon()
    print(id(obj3))


main()