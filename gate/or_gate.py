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

        for input in self.inputs:
            o = input.logic(depend + [self])
            if o == 1:
                self.output = 1
                if Or.DEBUGMODE:
                    print(self)
                return 1

        self.output = 0
        if Or.DEBUGMODE:
            print(self)
        return 0
