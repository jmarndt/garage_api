from gpiozero import DigitalOutputDevice


def momentary_activation(relay: DigitalOutputDevice, duration=0.1, count=1) -> None:
    relay.blink(on_time=duration, n=count)


def create_control(gpioPin: int, active_high=False, initial_value=False) -> DigitalOutputDevice:
    return DigitalOutputDevice(gpioPin, active_high=active_high, initial_value=initial_value)


if __name__ == "__main__":
    pass