from flipflop.flipflop import FlipFlop
from gate.not_gate import Not
from latch.d import D_Latch


class D_FlipFlop(FlipFlop):
    def __init__(self, clock, input):
        super().__init__(clock, input)

    def build(self):
        not1 = Not(self.clock)

        master = D_Latch(self.clock, self.input)
        slave = D_Latch(not1, master)

        self.output = slave.output
        self.outputp = slave.outputp
        self.gates = master.gates + slave.gates + [not1]

    def logic(self):
        self.output.logic()
