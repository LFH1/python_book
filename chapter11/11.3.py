from pathlib import Path
import json

# employee.py
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        self.annual_salary += amount
        print(f"{self.first_name} {self.last_name} received a raise. Annual salary is now: {self.annual_salary}")


# test_employee.py
from employee import Employee


def test_give_default_raise():
    emp = Employee('Alice', 'Johnson', 50000)
    emp.give_raise()
    assert emp.annual_salary == 55000


def test_give_custom_raise():
    emp = Employee('Bob', 'Smith', 60000)
    emp.give_raise(8000)
    assert emp.annual_salary == 68000

# test_employee_with_fixture.py
import pytest
from employee import Employee


@pytest.fixture
def employee():
    return Employee('John', 'Doe', 70000)


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 75000


def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 85000






