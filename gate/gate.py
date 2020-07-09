class Gate:
    def __init__(self, inputs: tuple):
        self.inputs = inputs
        self.output = None

    def logic(self):
        pass

    def set_inputs(self, inputs):
        self.inputs = inputs
