# Smart Parking System:
# • Create classes Vehicle, ParkingSpot, and ParkingLot.
# • Create multiple objects (vehicles, spots, parking lot).
# • Demonstrate object creation, attribute initialization, and method calls.
# • Make sensitive attributes private (e.g., license plate, owner name, spot status).
# • Provide getter/setter methods to access/update them safely.
# • Show that direct access fails but methods work.
# • Vehicle is the base class.
# • Derived classes:
# Bike (extra attribute: helmet_required)
# Car (extra attribute: seats)
# SUV (extra attribute: four_wheel_drive)
# Truck (extra attribute: max_load_capacity)
# • Each child class overrides display() to print its own details.
# • Create a list of different vehicle objects (Bike, Car, SUV, Truck).
# • Iterate and call display() → each object responds differently.
# • Implement a calculate_parking_fee() method:
# Bike → ₹20/hour
# Car → ₹50/hour
# SUV → ₹70/hour
# Truck → ₹100/hour
# • Demonstrate runtime polymorphism by calling the method on different objects.
# • Create an abstract class/interface Payment (using abc module).
# • Define an abstract method process_payment(amount).
# • Create child classes:
# CashPayment
# CardPayment
# UPIPayment
# • Demonstrate abstraction by processing payments differently (just print “Paid ₹X via UPI”).
# Task 1: Vehicle Classes
# Implement base and derived vehicle classes with encapsulation.
# Override display() and calculate_parking_fee().
# Task 2: ParkingSpot Class
# Implement ParkingSpot with size restrictions (S, M, L, XL).
# Methods: assign_vehicle(), remove_vehicle().
# Ensure vehicle type fits correct spot size (Bike → S+, Car → M+, SUV → L+, Truck → XL only).
# Task 3: ParkingLot Class
# Store multiple parking spots.
# Methods:
# add_spot() → add new parking spots.
# show_spots() → display all spots and their status.
# park_vehicle(vehicle) → find suitable spot and park.
# unpark_vehicle(vehicle) → remove from spot and calculate fee.
# Task 4: Payment (Abstraction + Polymorphism)
# When un-parking a vehicle, calculate fee (based on hours).
# Ask user for payment method → process payment using appropriate child class.
# Task 5: Main Program
# Create a parking lot with mixed spots.
# Create multiple vehicle objects.
# Park/unpark vehicles.
# Demonstrate encapsulation, inheritance, polymorphism, and abstraction throughout.
from abc import ABC,abstractmethod

class Vehicle:
    def __init__(self,name,color,license_plate ,owner_name):
        self.name = name
        self.color = color
        self.__license_plate = license_plate 
        self.__owner_name = owner_name  

    def get_license_plate(self):
        return self.__license_plate

    def get_owner_name(self):
        return self.__owner_name

    def set_license_plate(self,new):
        self.__license_plate=new

    def set_owner_name(self,new):
        self.__owner_name=new

    def display(self):
        pass

    def parking_fee(self,hours):
        pass

class Bike(Vehicle):
    def __init__(self, name, color,license_plate ,owner_name,helmet_required):
        super().__init__(name, color,license_plate ,owner_name)
        self.helmet_required = helmet_required

    def parking_fee(self,hours):
        return hours*20

    def display(self):
        print(f"Bike Properties: \n name : {self.name}\n color: {self.color}\n helmet required: {self.helmet_required}\nlicense_plate: {self.get_license_plate()}\n owner name: {self.get_owner_name()}")

class Car(Vehicle):
    def __init__(self, name, color,license_plate ,owner_name,seats):
        super().__init__(name, color,license_plate ,owner_name)
        self.seats = seats

    def parking_fee(self,hours):
        return hours*50

    def display(self):
         print(f"Car Properties: \n name : {self.name}\n color: {self.color}\n no. of seats: {self.seats}\nlicense_plate: {self.get_license_plate()}\n owner name: {self.get_owner_name()}")

class SUV(Vehicle):
    def __init__(self, name, color,license_plate ,owner_name,four_wheel_drive):
        super().__init__(name, color,license_plate ,owner_name)
        self.four_wheel_drive=four_wheel_drive

    def parking_fee(self,hours):
        return hours*70

    def display(self):
         print(f"SUV Properties: \n name : {self.name}\n color: {self.color}\n four wheel drive: {self.four_wheel_drive}\nlicense_plate: {self.get_license_plate()}\n owner name: {self.get_owner_name()}")

class Truck(Vehicle):
    def __init__(self, name, color,license_plate ,owner_name,max_load_capacity):
        super().__init__(name, color,license_plate ,owner_name)
        self.max_load_capacity=max_load_capacity

    def parking_fee(self,hours):
        return hours*100

    def display(self):
         print(f"Truck Properties: \n name : {self.name}\n color: {self.color}\n max load: {self.max_load_capacity}\nlicense_plate: {self.get_license_plate()}\n owner name: {self.get_owner_name()}")


class ParkingSpot:
    SIZE_ORDER = {"S": 1, "M": 2, "L": 3, "XL": 4}
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.__size = size 
        self.__vehicle = None

    def get_size(self):
        return self.__size

    def get_vehicle(self):
        return self.__vehicle

    def assign_vehicle(self, vehicle):
        if self.__vehicle is not None:
            print(f"Spot {self.spot_id} is already occupied.")
            return False
        if not self._can_fit_vehicle(vehicle):
            print(f"Vehicle {vehicle.name} does not fit in spot size {self.__size}.")
            return False
        self.__vehicle = vehicle
        print(f"Vehicle {vehicle.name} parked in spot {self.spot_id}.")
        return True

    def remove_vehicle(self):
        if self.__vehicle is None:
            print(f"Spot {self.spot_id} is already empty.")
            return None
        vehicle = self.__vehicle
        self.__vehicle = None
        print(f"Vehicle {vehicle.name} removed from spot {self.spot_id}.")
        return vehicle

    def _can_fit_vehicle(self, vehicle):
        vehicle_type = type(vehicle).__name__
        required_size = {
            "Bike": "S",
            "Car": "M",
            "SUV": "L",
            "Truck": "XL"
        }
        vehicle_size = required_size.get(vehicle_type)
        if vehicle_size is None:
            return False
        return ParkingSpot.SIZE_ORDER[self.__size] >= ParkingSpot.SIZE_ORDER[vehicle_size]

    def status(self):
        if self.__vehicle:
            return f"Occupied by {self.__vehicle.name} ({self.__vehicle.get_license_plate()})"
        else:
            return "Empty"

    def display(self):
        print(f"Spot {self.spot_id} [{self.__size}] - {self.status()}")

class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def show_spots(self):
        print(f"Parking Lot: {self.name}")
        for spot in self.spots:
            spot.display()

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.get_vehicle() is None and spot._can_fit_vehicle(vehicle):
                success = spot.assign_vehicle(vehicle)
                return success
        print(f"No available spot for vehicle {vehicle.name}.")
        return False

    def unpark_vehicle(self, vehicle, hours, payment_method):
        for spot in self.spots:
            if spot.get_vehicle() == vehicle:
                fee = vehicle.parking_fee(hours)
                print(f"Parking fee for {vehicle.name} for {hours} hour(s): ₹{fee}")
                payment_method.process_payment(fee)
                spot.remove_vehicle()
                return True
        print(f"Vehicle {vehicle.name} not found in parking lot.")
        return False

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Cash.")

class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Card.")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI.")

def main():
    lots = ParkingLot("Parking Lot Slots")
    lots.add_spot(ParkingSpot("s1","S"))
    lots.add_spot(ParkingSpot("s2","S"))
    lots.add_spot(ParkingSpot("s3","S"))
    lots.add_spot(ParkingSpot("m1","M"))
    lots.add_spot(ParkingSpot("l1","L"))
    lots.add_spot(ParkingSpot("xl1","XL"))
    lots.add_spot(ParkingSpot("xl2","XL"))
    lots.show_spots()
    print()

    bike = Bike("Yamaha", "Red", "BIKE123", "Alice", helmet_required=True)
    car = Car("Honda City", "Blue", "CAR456", "Bob", seats=4)
    suv = SUV("Toyota Fortuner", "Black", "SUV789", "Charlie", four_wheel_drive=True)
    truck = Truck("Volvo", "White", "TRK101", "Dave", max_load_capacity=15)
    
    vehicles = [bike, car, suv, truck]
    for v in vehicles:
        v.display()
        print()

    # Demonstrate failed direct access to private attributes
    try:
        print(bike.__license_plate)
    except AttributeError:
        print("Cannot access bike.__license_plate directly!")

    try:
        print(car.__owner_name)
    except AttributeError:
        print("Cannot access car.__owner_name directly!")

    print("Accessing private attributes via getter methods works:")
    print(f"Bike license plate: {bike.get_license_plate()}")
    print(f"Car owner name: {car.get_owner_name()}")
    print()

    lots.park_vehicle(bike)
    lots.park_vehicle(car)
    lots.park_vehicle(suv)
    lots.park_vehicle(truck)

    print()
    lots.show_spots()
    print()

    hours_parked = 3
    for v in vehicles:
        fee = v.parking_fee(hours_parked)
        print(f"{v.name} parking fee for {hours_parked} hours: ₹{fee}")

    print()
    
    payments = [CashPayment(), CardPayment(), UPIPayment(), CardPayment()]

    for v, payment in zip(vehicles, payments):
        lots.unpark_vehicle(v, hours_parked, payment)
        print()

    lots.show_spots()

if __name__=="__main__":
    main()
