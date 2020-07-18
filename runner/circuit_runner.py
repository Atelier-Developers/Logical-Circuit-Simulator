from adder.full_adder import FullAdder
from comparator.comparator import Comparator
from decoder.decoder_mxn import Decoder_nxm
from flipflop.d import D_FlipFlop
from latch.d import D_Latch
from multiplexer.mux2x1 import Mux2x1
from multiplexer.mux4x2 import Mux4x2
from multiplexer.mux_mxn import Mux_mxn
from signals.signal import Signal


class CircuitRunner:
    NOT_GATE = [
        D_FlipFlop,
        D_Latch,
        FullAdder,
        Comparator,
        Decoder_nxm,
        Mux_mxn,
        Mux2x1,
        Mux4x2
    ]

    @staticmethod
    def run(gates_list, clock: Signal = None, n_pulse=None, display=None):
        if n_pulse is None:
            n_pulse = -1
        if clock is None:
            depend = []
            for gate in gates_list:
                gate.logic(depend)

            if display:
                for lst in display:
                    if type(lst[0]) in CircuitRunner.NOT_GATE:
                        print("".join([str(r.output.output) for r in lst]))
                    else:
                        print("".join([str(r.output) for r in lst]))
        else:
            while not n_pulse == 0:
                n_pulse -= 1
                clock.pulse()

                depend = []
                for gate in gates_list:
                    gate.logic(depend)

                if display:
                    for lst in display:
                        if type(lst[0]) in CircuitRunner.NOT_GATE:
                            print("".join([str(r.output.output) for r in lst]))
                        else:
                            print("".join([str(r.output) for r in lst]))
