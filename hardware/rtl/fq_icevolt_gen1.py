from amaranth import *
from amaranth.back import verilog

class FQIceVoltGen1(Elaboratable):
    def __init__(self):
        self.clk_sys = Signal()
        self.reset_n = Signal()
        self.xstar_mailbox_in = Signal(32)
        self.xstar_mailbox_out = Signal(32)
        self.gpu_fps_lock_mode = Signal(2)
        self.liquid_cool_req = Signal()

    def elaborate(self, platform):
        m = Module()
        with m.If(self.xstar_mailbox_in == 0x47414D45):
            m.d.sync += self.gpu_fps_lock_mode.eq(0b10)
            m.d.sync += self.liquid_cool_req.eq(1)
            m.d.sync += self.xstar_mailbox_out.eq(0x00020000)
        with m.Else():
            m.d.sync += self.gpu_fps_lock_mode.eq(0b01)
            m.d.sync += self.liquid_cool_req.eq(0)
            m.d.sync += self.xstar_mailbox_out.eq(0x00010000)
        return m
