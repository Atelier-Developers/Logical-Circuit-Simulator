from gate.gate import Gate


class And(Gate):
    DEBUGMODE = False

    def __init__(self, inputs: tuple, name="And_Gate"):
        super().__init__(inputs, name)

    def logic(self, depend=None):
        if depend is None:
            depend = []
        if self in depend:
            if And.DEBUGMODE:
                print(self)
            return self.output

        result = 1
        depend.append(self)
        for input in self.inputs:
            current = input.logic(depend)
            if current is not None:
                result = result and current

        self.output = result
        if And.DEBUGMODE:
            print(self)
        return self.output
