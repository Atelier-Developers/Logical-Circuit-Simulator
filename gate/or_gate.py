from gate.gate import Gate


class Or(Gate):
    def __init__(self, inputs: tuple):
        super().__init__(inputs)

    def logic(self):
        for input in self.inputs:
            if input.output == 1:
                self.output = 1
                return 1
        self.output = 0
        return 0