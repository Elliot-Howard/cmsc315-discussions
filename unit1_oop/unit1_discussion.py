
"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented
programming (OOP) concepts in Python.
Complete the TODO sections to demonstrate inheritance,
namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information
#   about the object.
#
# Replace the pass statement with your implementation.

class Vehicle:
    vehicle_type = "Motor Vehicle"

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Vehicle: {self.make} {self.model}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Car(Vehicle):
    category = "Passenger Car"

    def __init__(self, make, model, year, features):
        super().__init__(make, model)
        self.year = year
        self.features = list(features)

    def display_info(self):
        return (
            f"Car: {self.year} {self.make} {self.model}, "
            f"Features: {self.features}"
        )

    # Student-created extension:
    # Add a new feature to the car.
    def add_feature(self, feature):
        if not isinstance(feature, str) or not feature.strip():
            print("Invalid feature.")
            return

        self.features.append(feature.strip())
        print(f"Added feature: {feature.strip()}")


# TODO 3:
# Create a function that demonstrates class namespaces
# and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after creation.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    car1 = Car("Toyota", "Camry", 2022, ["Bluetooth"])
    car2 = Car("Honda", "Civic", 2023, ["Backup Camera"])

    print("Class variable:", Car.category)
    print("Object class variable:", car1.category)

    # This attribute belongs only to car1.
    car1.owner = "Alex"

    print("Car 1 namespace:", car1.__dict__)
    print("Car 2 namespace:", car2.__dict__)

    print("Class namespace:")
    print("Category:", Car.__dict__["category"])
    print("Class attributes:", list(Car.__dict__.keys()))


# TODO 4:
# Create a function that demonstrates shallow copying
# and deep copying.
#
# Requirements:
# - Create an object containing nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original, shallow copy, and deep copy.
# - Explain the difference using comments.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = Car(
        "Ford",
        "Mustang",
        2024,
        ["Bluetooth", "GPS"]
    )

    # A shallow copy shares the nested features list.
    shallow = copy(original)

    # A deep copy creates an independent features list.
    deep = deepcopy(original)

    print("Before modification:")
    print("Original:", original.display_info())
    print("Shallow:", shallow.display_info())
    print("Deep:", deep.display_info())

    # Modify nested mutable data in the original.
    original.features.append("Heated Seats")

    print("\nAfter modification:")
    print("Original:", original.display_info())
    print("Shallow:", shallow.display_info())
    print("Deep:", deep.display_info())

    # The shallow copy shares the original features list.
    # The deep copy has a separate list and does not change.


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one parent class object.
# - Create at least one child class object.
# - Demonstrate inheritance by calling methods.
# - Call the namespace demonstration function.
# - Call the copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    vehicle = Vehicle("Chevrolet", "Silverado")
    print(vehicle.display_info())
    print("Vehicle type:", vehicle.vehicle_type)

    print("\n=== Child Object ===")
    car = Car(
        "Toyota",
        "Corolla",
        2023,
        ["Bluetooth", "Backup Camera"]
    )

    print(car.display_info())
    print("Inherited vehicle type:", car.vehicle_type)
    print("Car category:", car.category)

    print("\n=== Student-Created Extension ===")
    car.add_feature("Heated Seats")
    print(car.display_info())

    # Additional test cases
    print("\n=== Additional Test Cases ===")

    car.add_feature("Sunroof")
    car.add_feature("")
    car.add_feature("   ")
    car.add_feature(123)

    print("Final car features:", car.features)

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
