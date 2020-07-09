from gate.gate import Gate


class Or(Gate):
    def __init__(self, inputs: tuple):
        super().__init__(inputs)

    def logic(self):
        if self.calc:
            return self.output
        self.calc = True
        for input in self.inputs:
            input.logic()
            if input.output == 1:
                self.output = 1
                return 1
        self.output = 0
        self.calc = False
        return 0