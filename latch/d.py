from gate.and_gate import And
from gate.not_gate import Not
from gate.or_gate import Or
from latch.latch import Latch


class D_Latch(Latch):
    def __init__(self, clock, input):
        super().__init__(clock, input)

    def build(self):
        not0 = Not(self.input)
        and1 = And((self.input, self.clock))
        and2 = And((not0, self.clock))

        or1 = Or(None)
        or2 = Or(None)
        not1 = Not(or1)
        not2 = Not(or2)
        or1.set_inputs((not2, and2))
        or2.set_inputs((not1, and1))

        self.output = or1
        self.outputp = or2

        self.gates = [not0, and1, and2, or1, or2, not1, not2, or1, or2]

    def logic(self):
        self.output.logic()
