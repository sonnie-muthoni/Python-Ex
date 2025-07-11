class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, salary, hourly_rate, hours_worked):
        super().__init__(emp_id, name, salary)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, salary, monthly_salary):
        super().__init__(emp_id, name, salary)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        total_salary = super().calculate_salary() + self.monthly_salary
        return total_salary

# Example usage
if __name__ == "__main__":
    emp1 = HourlyEmployee(1, "Alice", 0, 20, 160)
    print(f"{emp1.name}'s Salary: {emp1.calculate_salary()}")

    emp2 = SalariedEmployee(2, "Bob", 1000, 3000)
    print(f"{emp2.name}'s Salary: {emp2.calculate_salary()}")

















