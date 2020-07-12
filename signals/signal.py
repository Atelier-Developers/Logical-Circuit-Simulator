from gate.one_gate import One
from gate.zero_gate import Zero


class Signal:
    DEBUGMODE = True

    def __init__(self, init_val=Zero()):
        self.output = init_val

    def pulse(self):
        self.output = One() if self.output.logic() == 0 else Zero()

    def logic(self, depend=[]):
        o = self.output.logic()
        if Signal.DEBUGMODE:
            print(self)
        return o

    def __repr__(self):
        return f"Signal: {self.output.output}"
