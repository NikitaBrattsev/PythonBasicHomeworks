"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    
    def __init__(self,max_cargo: int):
        self.max_cargo = max_cargo
        super(Plane,self).__init__()

    def load_cargo(self,additional_load: int):
        if additional_load + self.cargo > self.max_cargo:
            raise CargoOverload
        self.cargo = self.cargo + additional_load

    def remove_all_cargo(self):
        self.cargo = 0

#if __name__ == "__main__":
    #plane = Plane(10)
    # print("Max cargo: ", plane.max_cargo)
    # plane.cargo = 5
    # plane.load_cargo(2)
    # print("cargo loaded: ", plane.cargo)
    # plane.remove_all_cargo()
    # print("Cargo removed:", plane.cargo)
    # print(plane.weight)
    # plane.weight = 5000
    