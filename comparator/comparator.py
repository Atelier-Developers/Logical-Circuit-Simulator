from gate.not_gate import Not
from gate.or_gate import Or
from gate.xor_gate import Xor


class Comparator:
    def __init__(self, inputs, n, name=None):
        if name is None:
            name = f"Comparator{n}"

        self.output = None
        self.inputs = inputs
        self.n = n
        self.name = name

        self.build()

    def build(self):
        xors = []
        for i in range(self.n):
            xors.append(Xor((self.inputs[0][i], self.inputs[1][i]), f"{self.name}_xor{i}"))

        or0 = Or(tuple(xors), f"{self.name}_or0")

        self.output = Not(or0, f"{self.name}_not")

    def logic(self, depend=[]):
        if self in depend:
            return self.output.output

        self.output.logic(depend + [self])
        return self.output.output

    def __repr__(self):
        return f"{self.name}: {self.output.output}"
