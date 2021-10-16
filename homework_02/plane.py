"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super(Plane,self).__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
    
    def __str__(self) -> str:
        return f'Class: {__class__.__name__}; weight: {self.weight}; fuel: {self.fuel}; fuel_consuption: {self.fuel_consumption};Max cargo:{self.max_cargo}; Cargo: {self.cargo}'

    def load_cargo(self,additional_load: int):
        if additional_load + self.cargo > self.max_cargo:
            raise CargoOverload
        self.cargo = self.cargo + additional_load

    def remove_all_cargo(self):
        self.cargo = 0

# if __name__ == "__main__":
#     plane = Plane(50)
#     print(plane)
    # print("Max cargo: ", plane.max_cargo)
    # plane.cargo = 5
    # plane.load_cargo(2)
    # print("cargo loaded: ", plane.cargo)
    # plane.remove_all_cargo()
    # print("Cargo removed:", plane.cargo)
    # print(plane.weight)
    # plane.weight = 5000
    