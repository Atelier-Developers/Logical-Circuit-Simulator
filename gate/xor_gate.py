from gate.gate import Gate


class Xor(Gate):
    DEBUGMODE = True

    def __init__(self, inputs: tuple, name="Xor_Gate"):
        super().__init__(inputs, name)

    def logic(self, depend=[]):
        if self in depend:
            if Xor.DEBUGMODE:
                print(self)
            return self.output

        o0 = self.inputs[0].logic(depend + [self])
        o1 = self.inputs[1].logic(depend + [self])

        self.output = 0 if o0 == o1 else 1

        if Xor.DEBUGMODE:
            print(self)
        return self.output
