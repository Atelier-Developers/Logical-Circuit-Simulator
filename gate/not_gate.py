from gate.gate import Gate


class Not(Gate):
    def __init__(self, input):
        super().__init__(input)

    def logic(self):
        if self.calc:
            return self.output
        self.calc = True
        self.inputs.logic()
        self.output = 0 if self.inputs.output == 1 else 1
        self.calc = False
        return self.output
