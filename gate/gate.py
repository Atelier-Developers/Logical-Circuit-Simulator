class Gate:
    def __init__(self, inputs, name="Gate"):
        self.inputs = inputs
        self.output = None
        self.calc = False
        self.name = name

    def logic(self):
        pass

    def set_inputs(self, inputs):
        self.inputs = inputs

    def __repr__(self):
        return f"{self.name}: {self.output}"
