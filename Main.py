class Car:
    def __init__(self, speed=0, fuel=100):
        self.__speed = 0
        self.__fuel = max(0, fuel)

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if 0 <= speed <= 200:
            self.__speed = speed
        else:
            print("Speed must be between 0 and 200.")

    def get_fuel(self):
        return self.__fuel

    def set_fuel(self, fuel):
        if fuel >= 0:
            self.__fuel = fuel
        else:
            print("Fuel cannot be negative.")


# Example usage
car = Car()
car.set_speed(180)
print("Speed:", car.get_speed())
car.set_fuel(-10)
print("Fuel:", car.get_fuel())
