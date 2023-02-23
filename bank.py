class Bank:
    def __init__(self, name, head_name, coef):
        self.name = name
        self.head_name = head_name
        self.__coef = coef

    @property
    def coef(self):
        return self.__coef

    @coef.setter
    def coef(self, value):
        if 0.0 <= value <= 100.0:
            self.__coef = value
        else:
            raise ValueError("coef - годовая ставка (%), значение должно лежать между 0.0 и 100.0")

    def calculate(self, client, n):
        if n <= 0:
            raise ValueError("n - должен быть положительным целым числом.")
        
        x = money * (1 + coef)^n
        return x

u1 = Bank("Sabi", "Sabi", 50)

class Client:
    def __init__(self, name, id, bank, money):
        self.name = name
        self.id = id
        self.bank = bank
        self.__money = money
        self.__money_after_year = None
    
    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, value):
        self.__money = value
    
    @property
    def money_after_year(self):
        if self.__money_after_year is None:
            self.__money_after_year = self.bank.calculate(self, 1)
        return self.__money_after_year
    
    def invest(self, amount):
        if amount <= 0:
            print("нельзя вводить отрицательное число")
        else:
            self.__money += amount
    
    def take_money(self, amount):
        if amount <= 0:
            print("нельзя вводить отрицательное число")
        elif amount > self.__money:
            print("Слишком мало денег")
        else:
            self.__money -= amount
