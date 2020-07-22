import random


class Dice:
    def roll_dice(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return x, y


value = Dice()
print(value.roll_dice())
