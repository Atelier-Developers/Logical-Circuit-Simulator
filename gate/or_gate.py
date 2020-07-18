from gate.gate import Gate


class Or(Gate):
    DEBUGMODE = False

    def __init__(self, inputs: tuple, name="Or_Gate"):
        super().__init__(inputs, name)

    def logic(self, depend=[]):
        if self in depend:
            if Or.DEBUGMODE:
                print(self)
            return self.output

        result = 0
        depend.append(self)
        for input in self.inputs:
            current = input.logic(depend)
            if current is not None:
                result = result or current

        self.output = result
        if Or.DEBUGMODE:
            print(self)
        return self.output
