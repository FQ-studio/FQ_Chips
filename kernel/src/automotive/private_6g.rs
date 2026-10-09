pub struct Private6gUnlicensedEngine {
    spectrum_reg: usize,
    crypto_key_reg: usize,
}

impl Private6gUnlicensedEngine {
    pub const fn new() -> Self {
        Self {
            spectrum_reg: 0x6000_1000,
            crypto_key_reg: 0x6000_1004,
        }
    }

    pub unsafe fn init_unlicensed_private_link(&self) {
        core::ptr::write_volatile(self.spectrum_reg as *mut u32, 0x0060_0000);
        core::ptr::write_volatile(self.crypto_key_reg as *mut u32, 0x1A2B_3C4D);
    }
}
