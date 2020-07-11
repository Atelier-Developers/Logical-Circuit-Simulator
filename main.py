from flipflop.d import D_FlipFlop
from gate.and_gate import And
from gate.or_gate import Or
from latch.d import D_Latch
from signals.signal import Signal

from gate.not_gate import Not


def turn_off_debug(every_thing=True):
    And.DEBUGMODE = every_thing
    Or.DEBUGMODE = every_thing
    D_FlipFlop.DEBUGMODE = every_thing
    D_Latch.DEBUGMODE = every_thing
    Not.DEBUGMODE = every_thing


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

    for _ in range(400):
        clock.pulse()
        bits[-1].logic()
        print("".join([str(b.q()) for b in bits]))


turn_off_debug(False)
johnson_counter()
