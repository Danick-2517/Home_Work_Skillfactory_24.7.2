import pytest
from app.calculator_file import Calculator

class Test_calculator:

    def setup_method(self):
        self.calculator_file=Calculator

    def test_multiply_succes(self):
        assert self.calculator_file.multiply(self,6,6)==36
    def test_division_succes(self):
        assert self.calculator_file.division(self,8,4)==2
    def test_subtraction_succes(self):
        assert self.calculator_file.subtraction(self,120,40)==80
    def test_adding_succes(self):
        assert self.calculator_file.adding(self,773,4)==777
