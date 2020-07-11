from gate.gate import Gate


class One(Gate):
    def __init__(self, name="One"):
        super().__init__((), name)
        self.output = 1

    def logic(self, depend=[]):
        self.output = 1
        return 1