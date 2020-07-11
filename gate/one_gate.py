from gate.gate import Gate


class One(Gate):
    def __init__(self, name="One"):
        super().__init__((), name)

    def logic(self):
        self.output = 1
        return 1