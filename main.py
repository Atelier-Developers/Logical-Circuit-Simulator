from flipflop.d import D_FlipFlop
from signals.signal import Signal

from gate.not_gate import Not

clock = Signal(cycle=1)
d1 = D_FlipFlop(clock, None)
not1 = Not(d1)
d1.set_input(not1)
d1.set()

print(d1.q())
clock.pulse()
d1.logic()
print(d1.q())
clock.pulse()
d1.logic()
print(d1.q())
clock.pulse()
d1.logic()
print(d1.q())
clock.pulse()
d1.logic()
print(d1.q())
clock.pulse()
d1.logic()
