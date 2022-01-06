class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.capacity = {}
        self.capacity['big'] = big
        self.capacity['medium'] = medium
        self.capacity['small'] = small

    def addCar(self, carType: int) -> bool:
        if carType == 3 and self.capacity['small'] != 0:
            self.capacity['small'] -= 1
            return True
        elif carType == 2 and self.capacity['medium'] != 0:
            self.capacity['medium'] -= 1
            return True
        elif carType == 1 and self.capacity['big'] != 0:
            self.capacity['big'] -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)