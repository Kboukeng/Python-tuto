from enum import Enum, auto


class yam(Enum):
    small = 10
    medium = 20
    big = 30


choise = yam.medium
print(choise.value)
