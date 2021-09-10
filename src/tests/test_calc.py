import pytest

from src.calc import Interpreter

@pytest.mark.parametrize("expression,expected_result", [('1+2', 3), ('2+8', 10), ('12+3', 15), ('13+2', 15), ('18+12', 30)])
def test_calc_adding_two_integers(expression, expected_result):
    interpreter = Interpreter(expression)

    result = interpreter.expr()

    assert result == expected_result