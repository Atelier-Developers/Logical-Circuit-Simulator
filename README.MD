# Logical Circuit Simulator in Python

This library help to simulate Sequential Logical Circuit. 
### How it works?
check out this [Paper](https://docs.google.com/document/d/1PxQw0eowU9g0zAxsIFedXjEQHsVnnVNxTFzNa7UyNtk/edit?usp=sharing)
![Image of circuit](http://s12.picofile.com/file/8402889692/circuit_work.gif)


## How to make your Circuit

**Step one:** Make your circuit and connect the gates.
**Step two:** Pass the circuit to the runner and All is done.

#### Important Warning: 
you should first determine flipflop, multiplexer, latch,... inputs then set or reset it.
consider this example:
```python
from flipflop.d import D_FlipFlop
from signals.signal import Signal
from gate.not_gate import Not

###### CORRECT WAY ##########
clock = Signal()             # Clock for pulse
d1 = D_FlipFlop(clock, None, "d1")  # make our D flipflop
not1 = Not(d1, "not")               # make not Gate with d1 output
d1.set_input(not1)                  # set not for flipflop input
d1.set()

###### INCORRECT WAY ##########
clock = Signal()             # Clock for pulse
d1 = D_FlipFlop(clock, None, "d1")  # make our D flipflop
not1 = Not(d1, "not")               # make not Gate with d1 output
d1.set()
d1.set_input(not1)                  # set not for flipflop input
```
### Runner Inputs:
```python
CircuitRunner.run(
    list_of_the_gates_that_should_run, # list of 32 flipflops of a register
    clock=clock, # a signal that can pulse
    n_pulse=20, # if its is None or negetive it pulse for ever, otherwise pulse n_pulse time
    display=[[]], # list of registers( a list of flipflops ), then its a list of lists. that print them after each pulse
)
```
### Sample combinational Circuit
not(x1 and x2) or x3
![Image of circuit](http://s12.picofile.com/file/8402887350/circuit1.png)

```python
from gate.and_gate import And
from gate.or_gate import Or
from gate.not_gate import Not
from runner.circuit_runner import CircuitRunner

x1, x2, x3 = Zero(), One(), Zero()
and1 = And((x1, x2), "x1 & x2")
not1 = Not(and1, "not")
or1 = Or((not1, x3), "or x3")

CircuitRunner.run([or1], display=[[or1]])
```

shorter way
```python
from gate.and_gate import And
from gate.or_gate import Or
from gate.not_gate import Not
from runner.circuit_runner import CircuitRunner

x1, x2, x3 = 0, 1, 0
circuit = Or((x3, Not(And((x1,x2)))))
CircuitRunner.run([or1], display=[[or1]])
```
### D Flipflop
Its a sample code of flipflop that its input connected to output by a not gate.
![Image of circuit](http://s12.picofile.com/file/8402887326/circuit2.png)

```python
from flipflop.d import D_FlipFlop
from signals.signal import Signal
from gate.not_gate import Not
from runner.circuit_runner import CircuitRunner

clock = Signal()             # Clock for pulse
d1 = D_FlipFlop(clock, None, "d1")  # make our D flipflop
not1 = Not(d1, "not")               # make not Gate with d1 output
d1.set_input(not1)                  # set not for flipflop input
d1.set()

CircuitRunner.run([d1], clock=clock, n_pulse=20, display=[[d1]])
```

### Johnson Counter n-bit
```python
from flipflop.d import D_FlipFlop
from signals.signal import Signal
from gate.not_gate import Not
from runner.circuit_runner import CircuitRunner

n = 50
clock = Signal()
bits = [D_FlipFlop(clock, None, f"d{i}") for i in range(n)]
for i in range(1, n):
    bits[i].set_input(bits[i - 1])
    bits[i].reset()

bits[0].set_input(Not(bits[-1], "not"))
bits[0].reset()
CircuitRunner.run([bits[0]], clock=clock, n_pulse=n*4, display=[bits])
```

### N-bit Adder
```python
from flipflop.d import D_FlipFlop
from signals.signal import Signal
from adder.full_adder import FullAdder
from gate.zero_gate import Zero
from runner.circuit_runner import CircuitRunner

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

    if a[n-i-1] == '0':
        d1[i].reset()
    else:
        d1[i].set()

    if b[n-1-i] == '0':
        d2[i].reset()
    else:
        d2[i].set()

CircuitRunner.run(res, clock=clock, n_pulse=3, display=[res])
```
