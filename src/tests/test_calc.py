import pytest

from src.calc import Interpreter


@pytest.mark.parametrize(
    "expression,expected_result",
    [("2", 2), ("12", 12)],
)
def test_calc_nop(expression, expected_result):
    interpreter = Interpreter(expression)

    result = interpreter.expr()

    assert result == expected_result


@pytest.mark.parametrize(
    "expression,expected_result",
    [("1 +2", 3), ("1+2", 3), ("2+8", 10), ("12+3", 15), ("13+2", 15), ("18+12", 30)],
)
def test_calc_adding_two_integers(expression, expected_result):
    interpreter = Interpreter(expression)

    result = interpreter.expr()

    assert result == expected_result


@pytest.mark.parametrize(
    "expression,expected_result",
    [("3-2", 1), ("12-2", 10), ("2- 8", -6), (" 12-3", 9), ("18-12", 6)],
)
def test_calc_subtraction_two_integers(expression, expected_result):
    interpreter = Interpreter(expression)

    result = interpreter.expr()

    assert result == expected_result


@pytest.mark.parametrize(
    "expression,expected_result",
    [
        ("1 +2 -1", 2),
        ("1-1-1", -1),
        ("2+8+12", 22),
        ("12+3-15", 0),
        ("15-15-2+22", 20),
        ("2+3+6+9+10+1+2-1", 32),
    ],
)
def test_calc_adding_or_subtracting_several_integers(expression, expected_result):
    interpreter = Interpreter(expression)

    result = interpreter.expr()

    assert result == expected_result


@pytest.mark.parametrize(
    "expression,expected_result",
    [("3*2", 6), (" 12*2", 24), ("10* 10", 100)],
)
def test_calc_multiply_two_integers(expression, expected_result):
    interpreter = Interpreter(expression)

    result = interpreter.expr()

    assert result == expected_result


@pytest.mark.parametrize(
    "expression,expected_result",
    [("6 / 2", 3), (" 12/2", 6), ("10/ 10", 1)],
)
def test_calc_division_two_integers(expression, expected_result):
    interpreter = Interpreter(expression)

    result = interpreter.expr()

    assert result == expected_result


@pytest.mark.parametrize(
    "expression,expected_result",
    [
        ("1 *2 / 1", 2),
        ("1*1*1", 1),
        ("2*8/4", 4),
        ("12/2*5", 30),
        ("15/15*2*2", 4),
    ],
)
def test_calc_multiply_or_divide_several_integers(expression, expected_result):
    interpreter = Interpreter(expression)

    result = interpreter.expr()

    assert result == expected_result


@pytest.mark.parametrize(
    "expression,expected_result",
    [
        ("1 + 2 / 1", 3),
        ("1*1+1-8*2+10", -4),
        ("2*8+4-2", 18),
        ("1+ 12 / 2 * 5", 31),
        ("12 - 8 / 2 * 1 * 2 / 8 + 1", 12),
    ],
)
def test_calc_add_subtrack_multiply_or_divide_several_integers(
    expression, expected_result
):
    interpreter = Interpreter(expression)

    result = interpreter.expr()

    assert result == expected_result


@pytest.mark.parametrize(
    "expression,expected_result",
    [("(1 + 2) / 1", 3), ("1*1+(1-8)*2+10", -3)],
)
def test_calc_using_parenthesis(expression, expected_result):
    interpreter = Interpreter(expression)

    result = interpreter.expr()

    assert result == expected_result
