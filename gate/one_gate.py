from gate.gate import Gate


class One(Gate):
    def __init__(self):
        super().__init__(())

    def logic(self):
        self.output = 1
        return 1