class Holiday:
    def __init__(self, name, day, month):
        self.name = name
        self.day = day
        self.month = month

    def __str__(self):
        return f"Happy {self.name} day!"

    def __eq__(self, mereke):
        if self.month == mereke.month:
            return True
        else:
            return False

    def __lt__(self, mereke):
        if self.month == mereke.month:
            return self.day < other.day
        else:
            return self.month < mereke.month

    def __le__(self, mereke):
        if self.month == mereke.month:
            return self.day <= mereke.day
        else:
            return self.month <= mereke.month

    def __gt__(self, mereke):
        if self.month == mereke.month:
            return self.day > mereke.day
        else:
            return self.month > mereke.month

    def __ge__(self, mereke):
        if self.month == mereke.month:
            return self.day >= mereke.day
        else:
            return self.month >= mereke.month

m1 = Holiday('New Year', 31,'December')
m2 = Holiday('My Birthday', 7, 'April')

print(m1)
print(m1 == m2)
print(m1 > m2)

class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self._salary = salary
        self.position = position

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def __str__(self):
        return f"{self.name} at position {self.position}"

sabi = Employee('Sabi', 150000, 'SMM')
laura = Employee('Laura', 250000, 'Manager')

print(sabi.get_salary())
sabi.set_salary(155000)
print(sabi.get_salary())

print(sabi)
print(laura)