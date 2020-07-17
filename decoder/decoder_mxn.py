from gate.and_gate import And
from gate.not_gate import Not


class Decoder_nxm:
    DEBUGMODE = False

    def __init__(self, inputs, n, name=None):
        if name is None:
            name = f"Decoder{n}x{2 ** n}"
        self.n = n
        self.inputs = inputs
        self.name = name

        self.outputs = None

        self.build()

    def build(self):
        i = []
        ip = []
        for j in range(self.n):
            i.append(self.inputs[j])
            ip.append(Not(self.inputs[j], f"{self.name}_sp{j}"))

        ands = []
        for j in range(2 ** self.n):
            j_bin = bin(j)[2:].zfill(self.n)
            ands.append(
                And(tuple([i[k] if j_bin[k] == '1' else ip[k] for k in range(self.n)]), f"{self.name}_and{j}")
            )

        self.outputs = ands

    def logic(self, depend=[]):
        for output in self.outputs:
            output.logic(depend + [self])
        if Decoder_nxm.DEBUGMODE:
            print(self)
        return self.outputs
