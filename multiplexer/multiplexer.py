class Multiplexer:
    def __init__(self, inputs, selectors, name="Multiplexer"):
        self.inputs = inputs
        self.selectors = selectors
        self.name = name

        self.output = None

    def q(self):
        return self.output.output

    def __repr__(self):
        return f"{self.name}: {self.q()}"

    def logic(self, depend=[]):
        pass
