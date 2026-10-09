pub struct SteeringTouchSensor {
    touch_bus_io: usize,
}

impl SteeringTouchSensor {
    pub const fn new() -> Self {
        Self { touch_bus_io: 0x4000_3000 }
    }

    pub unsafe fn
