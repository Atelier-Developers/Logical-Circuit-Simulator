from adder.adder import Adder
from gate.and_gate import And
from gate.or_gate import Or
from gate.xor_gate import Xor


class FullAdder(Adder):
    def __init__(self, inputs, cin, name="Full_Adder"):
        super().__init__(inputs, name)
        self.cin = cin

        if inputs:
            self.build()

    def build(self):
        a, b = self.inputs[0], self.inputs[1]
        cin = self.cin

        xor0 = Xor((a, b), f"{self.name}_xor0")
        xor1 = Xor((xor0, cin), f"{self.name}_xor1")

        and0 = And((cin, xor0), f"{self.name}_and0")
        and1 = And((a, b), f"{self.name}_and1")

        or0 = Or((and0, and1), f"{self.name}_or0")

        self.sum = xor1
        self.cout = or0

    def set_cin(self, cin):
        self.cin = cin
        self.build()

    def c(self):
        return self.cout.output

    def __repr__(self):
        return f"{self.name}: {self.s()}, {self.c()}"

    def logic(self, depend=[]):
        if self in depend:
            return self.s(), self.c()
        depend.append(self)
        self.sum.logic(depend)
        self.cout.logic(depend)

        return self.s(), self.c()
