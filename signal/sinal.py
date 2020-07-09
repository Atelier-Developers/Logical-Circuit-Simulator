class Signal:
    def __init__(self, cycle=None, frequency=None, init_val=0, ):
        self.cycle = cycle if cycle else 1 / frequency if frequency else None
        self.output = init_val

    def pulse(self):
        self.output = 0 if self.output == 1 else 1
