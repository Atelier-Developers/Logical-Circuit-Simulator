from gate.gate import Gate


class Adder:
    def __init__(self, inputs, name="Adder"):
        self.inputs = inputs
        self.sum: Gate = None
        self.cout: Gate = None
        self.name = name


    def logic(self, depend=[]):
        pass

    def build(self):
        pass

    def set_input(self, input):
        self.input = input
        self.build()

    def s(self):
        return self.sum.output

