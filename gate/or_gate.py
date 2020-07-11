from gate.gate import Gate


class Or(Gate):
    DEBUGMODE = True

    def __init__(self, inputs: tuple, name="Or_Gate"):
        super().__init__(inputs, name)

    def logic(self):
        if self.calc:
            if Or.DEBUGMODE:
                print(self)
            return self.output
        self.calc = True
        for input in self.inputs:
            input.logic()
            if input.output == 1:
                self.output = 1
                if Or.DEBUGMODE:
                    print(self)
                self.calc = False
                return 1
        self.output = 0
        self.calc = False
        if Or.DEBUGMODE:
            print(self)
        return 0
