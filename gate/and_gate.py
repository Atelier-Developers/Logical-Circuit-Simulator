from gate.gate import Gate


class And(Gate):
    DEBUGMODE = False

    def __init__(self, inputs: tuple, name="And_Gate"):
        super().__init__(inputs, name)

    def logic(self, depend=[]):
        if self in depend:
            if And.DEBUGMODE:
                print(self)
            return self.output

        for input in self.inputs:
            o = input.logic(depend + [self])
            if o == 0:
                self.output = 0
                if And.DEBUGMODE:
                    print(self)
                return 0

        self.output = 1
        if And.DEBUGMODE:
            print(self)
        return 1
