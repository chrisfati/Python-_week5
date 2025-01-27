
# Base class: Vehicle
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Derived class: Car
class Car(Vehicle):
    def move(self):
        print(f"{self.name} is Driving 🚗")

# Derived class: Bike
class Bike(Vehicle):
    def move(self):
        print(f"{self.name} is Pedaling 🚴")

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is Flying ✈️")

# Derived class: Boat
class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is Sailing 🚤")

# Function to demonstrate polymorphism
def demonstrate_vehicle_movement(vehicles):
    for vehicle in vehicles:
        vehicle.move()

# Example usage
def main():
    # Create instances of different vehicles
    car = Car("Tesla Model 3")
    bike = Bike("Mountain Bike")
    plane = Plane("Boeing 747")
    boat = Boat("Yacht")

    # List of vehicles
    vehicles = [car, bike, plane, boat]

    # Demonstrate polymorphism
    demonstrate_vehicle_movement(vehicles)

if __name__ == "__main__":
    main()
