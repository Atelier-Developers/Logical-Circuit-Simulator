from flipflop.flipflop import FlipFlop
from gate.not_gate import Not
from latch.d import D_Latch


class D_FlipFlop(FlipFlop):
    DEBUGMODE = True

    def __init__(self, clock, input, name="D_FlipFlop"):
        super().__init__(clock, input, name)

    def build(self):
        not1 = Not(self.clock)

        master = D_Latch(not1, self.input, f"{self.name}_M")  # Master
        slave = D_Latch(self.clock, master, f"{self.name}_S")  # Slave

        self.output = slave.output
        self.outputp = slave.outputp
        self.gates = master.gates + slave.gates + [not1]

    def logic(self, depend=[]):
        if self in depend:
            return self.q()
        self.output.logic(depend + [self])
        if D_FlipFlop.DEBUGMODE:
            print(self)
        return self.q()
