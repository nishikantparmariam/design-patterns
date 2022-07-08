class BaseGateState:

    def enter(self):
        raise NotImplementedError

    def payOK(self):
        raise NotImplementedError

    def payFailed(self):
        raise NotImplementedError


class Gate:

    def __init__(self):
        self.state = ClosedGateState(self)

    def enter(self):
        self.state.enter()

    def payOK(self):
        self.state.payOK()

    def payFailed(self):
        self.state.payFailed()

    def stateState(self, state):
        self.state = state


class OpenGateState(BaseGateState):

    def __init__(self, gate):
        self.gate = gate

    def enter(self):
        self.gate.stateState(ClosedGateState(self.gate))

    def payOK(self):
        pass

    def payFailed(self):
        pass

class ClosedGateState(BaseGateState):
    
    def __init__(self, gate):
        self.gate = gate

    def enter(self):
        pass

    def payOK(self):
        self.gate.stateState(OpenGateState(self.gate))

    def payFailed(self):
        pass


###########################

