from modules.calculator import evaluate_expr


def test_basic_eval():
    assert evaluate_expr('2+3') == 5
    assert round(evaluate_expr('sin(0)'), 6) == 0