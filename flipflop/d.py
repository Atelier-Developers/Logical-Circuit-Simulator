from flipflop.flipflop import FlipFlop
from gate.not_gate import Not
from latch.d import D_Latch


class D_FlipFlop(FlipFlop):
    DEBUGMODE = False
    GATE_LVL = True

    def __init__(self, clock, input, name="D_FlipFlop"):
        super().__init__(clock, input, name)
        if D_FlipFlop.GATE_LVL:
            self.master: D_Latch = None
            self.slave: D_Latch = None
        else:
            self.last_clock = 0

    def build(self):
        if not D_FlipFlop.GATE_LVL:
            return
        not1 = Not(self.clock, f"{self.name}_M_ncp")

        self.master = D_Latch(not1, self.input, f"{self.name}_M")  # Master
        self.slave = D_Latch(self.clock, self.master, f"{self.name}_S")  # Slave

        self.output = self.slave.output
        self.outputp = self.slave.outputp

    def logic(self, depend=None):
        if depend is None:
            depend = []
        if self in depend:
            return self.output.output if D_FlipFlop.GATE_LVL else self.output

        if D_FlipFlop.GATE_LVL:
            depend.append(self)
            self.output.logic(depend)
            if D_FlipFlop.DEBUGMODE:
                print(self)
            return self.q()
        else:
            o = self.q()
            depend.append(self)
            if self.last_clock == 0 and self.clock.logic(depend) == 1:
                self.last_clock = self.clock.logic(depend)
                self.output = self.input.logic(depend)
            else:
                self.input.logic(depend)
                self.last_clock = self.clock.logic(depend)
            return o

    def q(self):
        if D_FlipFlop.GATE_LVL:
            return self.output.output
        else:
            return self.output

    def set(self):
        if D_FlipFlop.GATE_LVL:
            self.slave.output.output = 1
            self.slave.outputp.output = 0
            self.master.output.output = 1
            self.master.outputp.output = 0
        else:
            self.output = 1
            self.outputp = 0

    def reset(self):
        if D_FlipFlop.GATE_LVL:
            self.slave.output.output = 0
            self.slave.outputp.output = 1
            self.master.output.output = 0
            self.master.outputp.output = 1
        else:
            self.output = 0
            self.outputp = 1
