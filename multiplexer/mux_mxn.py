from gate.and_gate import And
from gate.not_gate import Not
from gate.or_gate import Or
from multiplexer.multiplexer import Multiplexer


class Mux_mxn(Multiplexer):
    DEBUGMODE = False

    def __init__(self, inputs, selectors, n, name=None):
        if name is None:
            name = f"Mux{2 ** n}x{n}"

        self.n = n
        super().__init__(inputs, selectors, name)

    def set_input(self, inputs):
        self.inputs = inputs
        self.build()

    def build(self):
        s = []
        sp = []
        for i in range(self.n):
            s.append(self.selectors[i])
            sp.append(Not(self.selectors[i], f"{self.name}_sp{i}"))

        ands = []
        for i in range(2 ** self.n):
            i_bin = bin(i)[2:].zfill(self.n)
            ands.append(
                And(tuple([s[j] if i_bin[j] == '1' else sp[j] for j in range(self.n)])
                    + (self.inputs[i],),
                    f"{self.name}_and{i}")
            )

        or0 = Or(tuple(ands), f"{self.name}_or0")

        self.output = or0

    def logic(self, depend=None):
        if depend is None:
            depend = []
        if self in depend:
            return self.output.output
        depend.append(self)
        self.output.logic(depend)
        if Mux_mxn.DEBUGMODE:
            print(self)

        return self.output.output

    def get_output(self):
        return self.output.output
