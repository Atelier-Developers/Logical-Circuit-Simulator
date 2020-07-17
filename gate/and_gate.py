from gate.gate import Gate


class And(Gate):
    DEBUGMODE = False

    def __init__(self, inputs: tuple, name="And_Gate"):
        super().__init__(inputs, name)

    def logic(self, depend=[]):
        if self in depend:
            if And.DEBUGMODE:
                print(self)
            return self.output

        result = 1
        for input in self.inputs:
            current = input.logic(depend + [self])
            if current is not None:
                result = result and current
            # if o == 0:
            #     self.output = 0
            #     if And.DEBUGMODE:
            #         print(self)
            #     return 0

        self.output = result
        if And.DEBUGMODE:
            print(self)
        return self.output
