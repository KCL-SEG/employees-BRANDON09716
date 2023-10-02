class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name


class MonthlySalaryEmployee(Employee):
    def __init__(self, name, monthly_salary, bonus=0):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def get_pay(self):
        return self.monthly_salary + self.bonus

    def __str__(self):
        if self.bonus > 0:
            return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked, bonus=0):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.bonus = bonus

    def get_pay(self):
        return (self.hourly_rate * self.hours_worked) + self.bonus

    def __str__(self):
        if self.bonus > 0:
            return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}."


class CommissionEmployee(Employee):
    def __init__(self, name, monthly_salary, hourly_rate, hours_worked, contracts_landed, commission_per_contract, bonus=0):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract
        self.bonus = bonus


    def get_pay(self):
        return (self.monthly_salary +self.hourly_rate * self.hours_worked+ self.contracts_landed * self.commission_per_contract) + self.bonus

    def __str__(self):
        if self.bonus > 0:
            return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."
        elif self.monthly_salary == 0:
            return f"{self.name} works on a contract of {self.hourly_rate} hours at {self.hours_worked}/hour and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."


# Create employees using the respective subclasses
billie = MonthlySalaryEmployee('Billie', 4000)
charlie = HourlyEmployee('Charlie', 25, 100)
renee = CommissionEmployee('Renee', 3000, 0,0,4, 200)
jan = CommissionEmployee('Jan', 0,150, 25, 3, 220)
robbie = MonthlySalaryEmployee('Robbie', 2000, 1500)
ariel = HourlyEmployee('Ariel', 30, 120, 600)
