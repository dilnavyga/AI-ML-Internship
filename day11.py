# Task 2: Inheritance Practice 
# 1. Create class Animal  
# 2. Create class Dog inheriting Animal  
# 3. Add method sound() 
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog1 = Dog()
dog1.eat()      
dog1.sound()  

# Task 3: Method Overriding 
# 1. Parent class → Vehicle  
# 2. Child class → Car  
# 3. Override method start() 
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting")

car1 = Car()
car1.start()

# Task 4: Encapsulation Practice 
# 1. Create class BankAccount  
# 2. Make balance private  
# 3. Create methods: deposit,withdraw,check balance 
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Balance:", self.__balance)

account = BankAccount(1000)

account.deposit(500)
account.withdraw(300)
account.check_balance()  

# Task 5: Combined Practice 
# Create: 
# • Class Person  
# • Class Employee (inherits Person)  
# • Add:name,salary display details
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

emp1 = Employee("vyga", 80000)
emp1.display_details()
