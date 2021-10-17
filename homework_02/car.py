"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
# from homework_02.engine import Engine


class Car(Vehicle):
    engine: None

    def __init__(self, weight, fuel, fuel_consumption):
        super(Car, self).__init__(weight, fuel, fuel_consumption)

    # engine: Engine
    def set_engine(self, engine):
        self.engine = engine

# if __name__ == "__main__":
#     engine = Engine(3, 4)
#     car = Car(5, 100, 10)
#     car.set_engine(engine)
#     print(car.engine)
