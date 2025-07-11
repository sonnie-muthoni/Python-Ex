#store information about employees in a company
class Employee:
    def __init__(self, companyname, name, position):
        self.companyname = companyname
        self.name = name
        self.position = position

    # method to display employee details
    def display_details(self):
        employee = f"Company: {self.companyname}, Name: {self.name}, Position: {self.position}"
        return employee

# create instances of Employee
employee1 = Employee("TechSolutions Ltd", "Alice", "project manager")
employee2 = Employee("TechSolutions Ltd", "Bob", "junior developer")

# display employee details
print(employee1.display_details())
print(employee2.display_details())




