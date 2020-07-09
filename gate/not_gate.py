from gate.gate import Gate


class Not(Gate):
    def __init__(self, input):
        super().__init__(input)

    def logic(self):
        self.output = 0 if self.inputs == 1 else 1
