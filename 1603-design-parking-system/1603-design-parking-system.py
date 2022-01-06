class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigCapacity = big
        self.mediumCapacity = medium
        self.smallCapacity = small

    def addCar(self, carType: int) -> bool:
        if carType == 3 and self.smallCapacity != 0:
            self.smallCapacity -= 1
            return True
        elif carType == 2 and self.mediumCapacity != 0:
            self.mediumCapacity -= 1
            return True
        elif carType == 1 and self.bigCapacity != 0:
            self.bigCapacity -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)