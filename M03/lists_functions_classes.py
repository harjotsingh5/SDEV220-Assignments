class Vehicle:
    def __init__ (self, car):
        self.vehicle_type = car

class Automobile(Vehicle):
    def __init__ (self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def main():

    vehicle_type = input("What type of vehicle do you drive (car/truck/bike/plane/boat/broomstick): ")

    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2/4): ")
    roof = input("What kind of roof (solid/sun): ")

    vehicle = Automobile(vehicle_type, year, make, model, doors, roof)

    print("-------------------------")
    print("Vehicle type:", vehicle.vehicle_type)
    print("Year:", vehicle.year)
    print("Make:", vehicle.make)
    print("Model:", vehicle.model)
    print("Doors:", vehicle.doors)
    print("Roof:", vehicle.roof)
    print("-------------------------")

main()
