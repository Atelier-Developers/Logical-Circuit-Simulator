from gate.gate import Gate


class Not(Gate):
    DEBUGMODE = False

    def __init__(self, input, name="Not_Gate"):
        super().__init__(input, name)

    def logic(self, depend=[]):
        if self in depend:
            if Not.DEBUGMODE:
                print(self)
            return self.output

        depend.append(self)
        o = self.inputs.logic(depend)
        self.output = 0 if o == 1 else 1
        if Not.DEBUGMODE:
            print(self)
        return self.output
