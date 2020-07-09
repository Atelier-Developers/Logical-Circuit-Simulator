from gate.gate import Gate


class Zero(Gate):
    def __init__(self):
        super().__init__(())

    def logic(self):
        self.output = 0
        return 0