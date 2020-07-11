class FlipFlop:
    def __init__(self, clock, input, name="FlipFlop"):
        self.clock = clock
        self.input = input
        self.gates = []
        self.output = None
        self.outputp = None

        self.name = name

        self.build()

    def logic(self):
        pass

    def build(self):
        pass

    def set_input(self, input):
        self.input = input
        self.build()

    def set(self):
        self.output.output = 1
        self.outputp.output = 0

    def reset(self):
        self.output.output = 0
        self.outputp.output = 1

    def q(self):
        return self.output.output

    def __repr__(self):
        return f"{self.name}: {self.output}"
