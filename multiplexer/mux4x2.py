from gate.and_gate import And
from gate.not_gate import Not
from gate.or_gate import Or
from multiplexer.multiplexer import Multiplexer


class Mux4x2(Multiplexer):
    DEBUGMODE = False

    def __init__(self, inputs, selectors, name="Mux4x2"):
        super().__init__(inputs, selectors, name)

    def build(self):
        s0 = self.selectors[0]
        s1 = self.selectors[1]
        s0p = Not(s0, f"{self.name}_s0p")
        s1p = Not(s1, f"{self.name}_s1p")

        and0 = And((self.inputs[0], s1p, s0p), f"{self.name}_and0")
        and1 = And((self.inputs[1], s1p, s0), f"{self.name}_and1")
        and2 = And((self.inputs[2], s1, s0p), f"{self.name}_and2")
        and3 = And((self.inputs[3], s1, s0), f"{self.name}_and3")

        or0 = Or((and0, and1, and2, and3), f"{self.name}_or0")

        self.output = or0

    def logic(self, depend=[]):
        self.output.logic(depend + [self])
        if Mux4x2.DEBUGMODE:
            print(self)
