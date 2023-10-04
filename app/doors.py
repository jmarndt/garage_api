from enum import Enum

from app.relay import create_control, momentary_activation


class GarageDoors(int, Enum):
    one = 1
    two = 2
    three = 3


BLACK_PIN = 5
WHITE_PIN = 6
GREY_PIN = 16
DOOR_RELAYS = {
    GarageDoors.one.value: create_control(BLACK_PIN),
    GarageDoors.two.value: create_control(WHITE_PIN),
    GarageDoors.three.value: create_control(GREY_PIN)
}


def door_control(door: GarageDoors) -> None:
    momentary_activation(DOOR_RELAYS[door])


if __name__ == "__main__":
    pass