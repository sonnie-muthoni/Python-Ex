#python class and objects
class Car:
    def __init__(self, brand, model, year=2025):
        self.brand = brand
        self.model = model
        self.year = year

    # methods
    def start_engine(self):
        return f"{self.brand} {self.model} {self.year} engine started"

    def stop_engine(self):
        return f"{self.brand} {self.model} {self.year} engine stopped"

# Example
if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla", 2022)
    print(my_car.start_engine())
    print(my_car.stop_engine())
    print(f"Car details: {my_car.brand} {my_car.model} {my_car.year}")

