from gate.one_gate import One
from gate.zero_gate import Zero


class Signal:
    def __init__(self, cycle=None, frequency=None, init_val=Zero()):
        self.cycle = cycle if cycle else 1 / frequency if frequency else None
        self.output = init_val

    def pulse(self):
        self.output = One() if self.output.logic() == 0 else Zero()

    def logic(self):
        return self.output.logic()