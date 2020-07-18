from flipflop.flipflop import FlipFlop
from gate.not_gate import Not
from latch.d import D_Latch


class D_FlipFlop(FlipFlop):
    DEBUGMODE = False

    def __init__(self, clock, input, name="D_FlipFlop"):
        super().__init__(clock, input, name)
        self.master: D_Latch = None
        self.slave: D_Latch = None

    def build(self):
        not1 = Not(self.clock, f"{self.name}_M_ncp")

        self.master = D_Latch(not1, self.input, f"{self.name}_M")  # Master
        self.slave = D_Latch(self.clock, self.master, f"{self.name}_S")  # Slave

        self.output = self.slave.output
        self.outputp = self.slave.outputp

    def logic(self, depend=[]):
        if self in depend:
            return self.output.output
        depend.append(self)
        self.output.logic(depend)
        if D_FlipFlop.DEBUGMODE:
            print(self)
        return self.q()

    def set(self):
        self.slave.output.output = 1
        self.slave.outputp.output = 0
        self.master.output.output = 1
        self.master.outputp.output = 0

    def reset(self):
        self.slave.output.output = 0
        self.slave.outputp.output = 1
        self.master.output.output = 0
        self.master.outputp.output = 1
