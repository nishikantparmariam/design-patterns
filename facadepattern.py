### LAW OF DEMETER --- PRINCIPLE OF LEAST KNOLEDGE --- TALK TO ONLY YOUR FRIENDS

# self.a.call()
# self.param.call()
# x = X(); x.call()
# self.call()

# self.a.b.call() # not allowed


class B:
    pass

class C:
    pass

class D:
    def __init__(self, c):
        self.c = C


class Facade:

    def __init__(self):
        self.b = B()        
        self.c = C()
        self.c.b = self.b
        self.d = D(self.c)

############


def main():

    facade = Facade()


main()





