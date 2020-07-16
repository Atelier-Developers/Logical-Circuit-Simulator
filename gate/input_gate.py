from gate.gate import Gate


class Input(Gate):
    def __init__(self, name="INPUTS"):
        super().__init__(None, name)
        self.output = 0

    def logic(self, depend=[]):
        return self.output
