"""Simple calculator module with history."""
from .utils import safe_input
import math

HISTORY = []


def evaluate_expr(expr: str):
    # Very limited safe eval: allow math functions and digits/operators
    allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith('_')}
    allowed_names.update({'abs': abs, 'round': round})

    try:
        # compile and eval in restricted namespace
        code = compile(expr, '<string>', 'eval')
        for name in code.co_names:
            if name not in allowed_names:
                raise NameError(f"Use of '{name}' is not allowed")

        result = eval(code, {'__builtins__': {}}, allowed_names)
        HISTORY.append((expr, result))
        return result
    except Exception as e:
        # Re-raise so caller can handle and show an error message
        raise e


def show_history():
    if not HISTORY:
        print('No history yet.')
        return

    for i, (expr, res) in enumerate(HISTORY, 1):
        print(f'{i}. {expr} = {res}')


def run():
    menu = (
        "\nCALCULATOR MENU:\n"
        "1. Evaluate Expression\n"
        "2. View History\n"
        "3. Back to Main Menu\n"
    )

    while True:
        print(menu)
        choice = safe_input('Choice: ').strip()

        if choice == '1':
            expr = safe_input('Enter expression (e.g. 2+3*sin(0.5)): ').strip()
            if not expr:
                continue
            try:
                res = evaluate_expr(expr)
                print('Result:', res)
            except Exception as e:
                print('Error evaluating expression:', e)

        elif choice == '2':
            show_history()

        elif choice == '3' or choice == '':
            break

        else:
            print('Invalid choice.')
