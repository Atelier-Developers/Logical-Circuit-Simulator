from gate.gate import Gate


class Zero(Gate):
    def __init__(self, name="Zero"):
        super().__init__((), name)

    def logic(self):
        self.output = 0
        return 0