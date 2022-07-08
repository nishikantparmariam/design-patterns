class BusAdaptee:

    def specificRequest(self):
        print('Calling the specific request')


class ITarget:

    def request(self):
        raise NotImplementedError



class BusTarget(ITarget):

    def __init__(self, busAdaptee):
        self.busAdaptee = busAdaptee

    def request(self):
        print('Converting the data..')
        self.busAdaptee.specificRequest()



####################


def main():

    # I am client
    target = BusTarget(BusAdaptee())
    target.request()

main()