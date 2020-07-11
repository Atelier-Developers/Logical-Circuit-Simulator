from gate.gate import Gate


class And(Gate):
    DEBUGMODE = True

    def __init__(self, inputs: tuple, name="And_Gate"):
        super().__init__(inputs, name)

    def logic(self):
        if self.calc:
            if And.DEBUGMODE:
                print(self)
            return self.output
        self.calc = True
        for input in self.inputs:
            input.logic()
            if input.output == 0:
                self.output = 0
                if And.DEBUGMODE:
                    print(self)
                return 0
        self.output = 1
        self.calc = False
        if And.DEBUGMODE:
            print(self)
        return 1
