from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False

    def __init__(self, weight=2000, fuel=100, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                print("Started")
            else:
                raise LowFuelError("Low fuel")
        else:
            print("Already started")

    def move(self, distance):
        if self.fuel_consumption * distance > self.fuel:
            raise NotEnoughFuel("Not enough fuel")


# if __name__ == "__main__":
    # car = Vehicle()
    # # car.started = True
    # car.fuel = 0
    # car.start()
    # car.move(50)
