#zad3

class Train:
    def __init__(self, speed: int, fuel: int):
        self.speed = speed
        self.fuel = fuel

    def opis(self):
        print(f"My speed is {self.speed}. I still have {self.fuel} l of fuel.")

    def __str__(self):
        return self.get_info()

    def speed_up(level_up_speed):
        self.speed = 10
        if level_up_speed <= 75:
            self.speed += level_up_speed
        else:
            return self.speed
        self.fuel = 1000
        self.fuel -= ((level_up_speed + self.speed) - self.speed) * (self.speed / 100)
        if self.fuel == 0:
            level_up_speed = 0

train_1 = Train(10, 1000)
train_1.opis()

def test_speed_up():
    assert speed_up(5) == 15
