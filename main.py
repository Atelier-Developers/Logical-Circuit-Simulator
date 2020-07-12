from adder.full_adder import FullAdder
from flipflop.d import D_FlipFlop
from gate.and_gate import And
from gate.one_gate import One
from gate.or_gate import Or
from gate.xor_gate import Xor
from gate.zero_gate import Zero
from latch.d import D_Latch
from multiplexer.mux2x1 import Mux2x1
from multiplexer.mux4x2 import Mux4x2
from signals.signal import Signal
from gate.not_gate import Not

import sys

sys.setrecursionlimit(1000)  # default is 1000


def turn_off_debug(every_thing=True):
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
    clock = Signal(cycle=1)
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
    clock = Signal(cycle=1)
    d1 = D_FlipFlop(clock, None, "d1")
    not1 = Not(d1, "not")
    d1.set_input(not1)
    d1.set()

    for _ in range(20):
        clock.pulse()
        d1.logic()
        print(f"{clock.output.output}: {d1.q()}")


def johnson_counter(n=100):
    clock = Signal(cycle=1)
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
    clock = Signal(cycle=1)
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

        if a[n-i-1] == '0':
            d1[i].reset()
        else:
            d1[i].set()

        if b[n-1-i] == '0':
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


turn_off_debug(False)
n_bit_adder()
#
#
# clock = Signal(cycle=1)
# d1 = D_FlipFlop(clock, None, "d1")
# d1.set_input(One())
# d1.reset()
#
# for _ in range(10):
#     clock.pulse()
#     d1.logic()
#     print(clock.output.output, d1.q())
