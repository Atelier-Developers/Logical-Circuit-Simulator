from gate.gate import Gate


class Not(Gate):
    DEBUGMODE = True

    def __init__(self, input, name="Not_Gate"):
        super().__init__(input, name)

    def logic(self):
        if self.calc:
            if Not.DEBUGMODE:
                print(self)
            return self.output
        self.calc = True
        self.inputs.logic()
        self.output = 0 if self.inputs.output == 1 else 1
        self.calc = False
        if Not.DEBUGMODE:
            print(self)
        return self.output
