"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engine


class Car(Vehicle):

    def __init__(self):
        super(Car,self).__init__()
    engine: Engine
    def set_engine(self,value,pistons):
        self.engine = Engine(value,pistons)

# if __name__ == "__main__":
#     car = Car()
#     car.set_engine(3,4)
#     print(car.engine)