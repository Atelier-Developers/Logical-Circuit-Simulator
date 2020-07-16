from adder.full_adder import FullAdder
from decoder.decoder_mxn import Decoder_nxm
from flipflop.d import D_FlipFlop
from gate.and_gate import And
from gate.input_gate import Input
from gate.one_gate import One
from gate.or_gate import Or
from gate.xor_gate import Xor
from gate.zero_gate import Zero
from latch.d import D_Latch
from multiplexer.mux2x1 import Mux2x1
from multiplexer.mux_mxn import Mux_mxn
from multiplexer.mux4x2 import Mux4x2
from signals.signal import Signal
from gate.not_gate import Not

import sys

sys.setrecursionlimit(1000)  # default is 1000


def turn_off_debug(every_thing=False):
    And.DEBUGMODE = every_thing
    Or.DEBUGMODE = every_thing
    Xor.DEBUGMODE = every_thing
    D_FlipFlop.DEBUGMODE = every_thing
    D_Latch.DEBUGMODE = every_thing
    Not.DEBUGMODE = every_thing
    Mux2x1.DEBUGMODE = every_thing
    Mux4x2.DEBUGMODE = every_thing
    Signal.DEBUGMODE = every_thing


def test1():
    clock = Signal()
    l1 = D_Latch(clock, None, "l1")

    l1.set_input(l1)
    l1.set()
    for _ in range(4):
        print("####################################")
        print(clock.output.output)
        print(l1.output.output)
        clock.pulse()
        l1.logic()


def test2():
    clock = Signal()
    d1 = D_FlipFlop(clock, None, "d1")
    not1 = Not(d1, "not")
    d1.set_input(not1)
    d1.set()

    for _ in range(20):
        clock.pulse()
        d1.logic()
        print(f"{clock.output.output}: {d1.q()}")


def johnson_counter(n=100):
    clock = Signal()
    bits = [D_FlipFlop(clock, None, f"d{i}") for i in range(n)]
    for i in range(1, n):
        bits[i].set_input(bits[i - 1])
        bits[i].reset()

    bits[0].set_input(Not(bits[-1], "not"))
    bits[0].reset()

    for _ in range(100):
        clock.pulse()
        bits[-1].logic()
        print("".join([str(b.q()) for b in bits]))


def multiplexer_test():
    mux = Mux4x2((One(), Zero(), One(), Zero()), (One(), Zero()), "my_mux")
    mux.logic()
    print(mux)


def n_bit_adder():
    clock = Signal()
    n = 5
    a, b = "01001", "01110"

    d1 = [D_FlipFlop(clock, None, f"a{i}") for i in range(n)]
    d2 = [D_FlipFlop(clock, None, f"b{i}") for i in range(n)]

    adder = [FullAdder(None, None, f"adder{i}") for i in range(n)]

    res = [D_FlipFlop(clock, None, f"r{i}") for i in range(n)]

    for i in range(n):
        d1[i].set_input(d1[i])
        d2[i].set_input(d2[i])
        adder[i].set_input((d1[i], d2[i]))
        adder[i].set_cin(Zero() if i == 0 else adder[i - 1].cout)

        res[i].set_input(adder[i].sum)
        res[i].reset()

        if a[n - i - 1] == '0':
            d1[i].reset()
        else:
            d1[i].set()

        if b[n - 1 - i] == '0':
            d2[i].reset()
        else:
            d2[i].set()

    for _ in range(3):
        clock.pulse()
        for i in range(n):
            res[i].logic()
    d1.reverse()
    d2.reverse()
    res.reverse()
    print("".join([str(r.q()) for r in d1]))
    print("".join([str(r.q()) for r in d2]))
    print("".join([str(r.q()) for r in res]))


def bitsToGates(bitString, inputs):
    for i in range(len(bitString)):
        inputs[i].output = 0 if bitString[i] == "0" else 1


def n_multiplexer_test():
    inputs = [Input() for _ in range(32)]
    selectors = [Input() for _ in range(5)]
    mux = Mux_mxn(inputs, selectors, 5)

    bitsToGates("11001110011100111001110011100101", inputs)

    for i in range(32):
        i_bin = bin(i)[2:].zfill(5)
        bitsToGates(i_bin, selectors)

        print(mux.logic(), end='')


def decoder_test():
    inputs = [Input() for _ in range(5)]
    dec = Decoder_nxm(inputs, 5)

    bitsToGates("11101", inputs)
    for i in range(2 ** 5):
        dec.outputs[i].logic()
    print("".join([str(o.output) for o in dec.outputs]))


turn_off_debug(False)
decoder_test()
