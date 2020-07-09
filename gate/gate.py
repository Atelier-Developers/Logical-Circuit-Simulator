class Gate:
    def __init__(self, inputs):
        self.inputs = inputs
        self.output = None
        self.calc = False

    def logic(self):
        pass

    def set_inputs(self, inputs):
        self.inputs = inputs
