# student.py

# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Student class inherits from Person
class Student(Person):
    def __init__(self, name, age, roll_no, grade, percentage):
        super().__init__(name, age)
        self.roll_no = roll_no
        self._grade = grade          # Protected attribute
        self.__percentage = percentage  # Private attribute

    def __str__(self):
        return f"{self.name},{self.age},{self.roll_no},{self._grade},{self.__percentage}"

    def get_details(self):
        return f"name={self.name}, age={self.age}, grade={self._grade}, percentage={self.__percentage}"

    # Property for percentage
    @property
    def percentage(self):
        return self.__percentage

    @percentage.setter
    def percentage(self, value):
        self.__percentage = value
