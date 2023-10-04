from enum import Enum

from app.relay import create_control, momentary_activation


class LightActions(str, Enum):
    on = "on"
    off = "off"
    up = "up"
    down = "down"
    half = "half"


ORANGE_PIN = 17
PURPLE_PIN = 27
BLUE_PIN = 22
YELLOW_PIN = 23
GREEN_PIN = 24
LIGHT_RELAYS = {
    LightActions.on.value: create_control(ORANGE_PIN),
    LightActions.off.value: create_control(PURPLE_PIN),
    LightActions.up.value: create_control(BLUE_PIN),
    LightActions.down.value: create_control(YELLOW_PIN),
    LightActions.half.value: create_control(GREEN_PIN)
}


def light_control(action: LightActions) -> None:
    momentary_activation(LIGHT_RELAYS[action])


if __name__ == "__main__":
    pass