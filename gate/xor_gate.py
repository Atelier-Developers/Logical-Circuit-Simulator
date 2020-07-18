from gate.gate import Gate


class Xor(Gate):
    DEBUGMODE = False

    def __init__(self, inputs: tuple, name="Xor_Gate"):
        super().__init__(inputs, name)

    def logic(self, depend=None):
        if depend is None:
            depend = []
        if self in depend:
            if Xor.DEBUGMODE:
                print(self)
            return self.output

        depend.append(self)
        o0 = self.inputs[0].logic(depend)
        o1 = self.inputs[1].logic(depend)

        self.output = 0 if o0 == o1 else 1

        if Xor.DEBUGMODE:
            print(self)
        return self.output
