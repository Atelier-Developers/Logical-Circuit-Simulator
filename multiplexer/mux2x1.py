from gate.and_gate import And
from gate.not_gate import Not
from gate.or_gate import Or
from multiplexer.multiplexer import Multiplexer


class Mux2x1(Multiplexer):
    DEBUGMODE = False

    def __init__(self, inputs, selectors, name="Mux2x1"):
        super().__init__(inputs, selectors, name)

    def build(self):
        and0 = And((self.inputs[0], Not(self.selectors[0], f"{self.name}_s0p")), f"{self.name}_and0")
        and1 = And((self.inputs[1], self.selectors[0]), f"{self.name}_and1")

        or0 = Or((and0, and1), f"{self.name}_or0")

        self.output = or0

    def logic(self, depend=None):
        if depend is None:
            depend = []
        if self in depend:
            return self.output.output
        depend.append(self)
        self.output.logic(depend)
        if Mux2x1.DEBUGMODE:
            print(self)

        return self.output.output
