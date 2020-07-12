from gate.and_gate import And
from gate.not_gate import Not
from gate.or_gate import Or
from latch.latch import Latch


class D_Latch(Latch):
    DEBUGMODE = True

    def __init__(self, clock, input, name="D_Latch"):
        super().__init__(clock, input, name)

    def build(self):
        not0 = Not(self.input, f"{self.name}_not0")
        and1 = And((not0, self.clock), f"{self.name}_and1")
        and2 = And((self.input, self.clock), f"{self.name}_and2")

        or1 = Or(None, f"{self.name}_or1")
        or2 = Or(None, f"{self.name}_or2")
        not1 = Not(or1, f"{self.name}_not1")
        not2 = Not(or2, f"{self.name}_not2")
        or1.set_inputs((not2, and1))
        or2.set_inputs((not1, and2))

        self.output = not1
        self.outputp = not2

    def logic(self, depend=[]):
        if self in depend:
            if D_Latch.DEBUGMODE:
                print(self)
            return self.output.output
        self.output.logic(depend + [self])
        if D_Latch.DEBUGMODE:
            print(self)
        return self.output.output
