from gate.gate import Gate


class Latch:
    def __init__(self, clock, input, name="Latch"):
        self.clock = clock
        self.input = input
        self.structure = None
        self.output: Gate = None
        self.outputp: Gate = None
        self.gates = []
        self.name = name

        self.build()

    def logic(self, depend=[]):
        pass

    def build(self):
        pass

    def set_input(self, input):
        self.input = input
        self.build()

    def set(self):
        self.output.output = 1
        self.outputp.output = 0

    def __repr__(self):
        return f"{self.name}: {self.output}"
