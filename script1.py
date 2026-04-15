import ast
import math


ALLOWED_NAMES = {
    name: getattr(math, name)
    for name in dir(math)
    if not name.startswith("_")
}
ALLOWED_NAMES["abs"] = abs
ALLOWED_NAMES["pi"] = math.pi
ALLOWED_NAMES["e"] = math.e


class SafeExpressionEvaluator(ast.NodeVisitor):
    def __init__(self, variable_value):
        self.variable_value = variable_value

    def visit(self, node):
        if isinstance(node, ast.Expression):
            return self.visit(node.body)
        return super().visit(node)

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
        if isinstance(node.op, ast.Pow):
            return left ** right
        if isinstance(node.op, ast.Mod):
            return left % right

        raise ValueError("Niedozwolony operator w wyrażeniu.")

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)

        if isinstance(node.op, ast.UAdd):
            return +operand
        if isinstance(node.op, ast.USub):
            return -operand

        raise ValueError("Niedozwolony operator jednoargumentowy.")

    def visit_Call(self, node):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Niedozwolone wywołanie funkcji.")

        func_name = node.func.id
        if func_name not in ALLOWED_NAMES:
            raise ValueError(f"Funkcja '{func_name}' nie jest dozwolona.")

        func = ALLOWED_NAMES[func_name]
        args = [self.visit(arg) for arg in node.args]
        return func(*args)

    def visit_Name(self, node):
        if node.id == "x":
            return self.variable_value
        if node.id in ALLOWED_NAMES:
            return ALLOWED_NAMES[node.id]
        raise ValueError(f"Niedozwolona nazwa: {node.id}")

    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Dozwolone są tylko liczby.")

    def generic_visit(self, node):
        raise ValueError("Niedozwolony element w wyrażeniu.")


def evaluate_expression(expression, x_value):
    tree = ast.parse(expression, mode="eval")
    evaluator = SafeExpressionEvaluator(x_value)
    return float(evaluator.visit(tree))


def numerical_derivative(expression, x_value, h=1e-6):
    return (evaluate_expression(expression, x_value + h) - evaluate_expression(expression, x_value - h)) / (2 * h)


def metoda_stycznych():
    wyrazenie = input("Podaj funkcję f(x) (np. x**3 - x - 2): ")

    x0 = float(input("Podaj punkt startowy x0: "))
    epsilon = float(input("Podaj dokładność epsilon (np. 1e-7): "))
    max_iter = int(input("Podaj maksymalną liczbę iteracji: "))

    print("\nRozpoczynam obliczenia metodą stycznych (Newtona)...\n")

    x_n = x0

    for i in range(max_iter):
        try:
            f_val = evaluate_expression(wyrazenie, x_n)
            df_val = numerical_derivative(wyrazenie, x_n)
        except Exception as e:
            print(f"Błąd podczas obliczania wyrażenia: {e}")
            return None

        if abs(df_val) < 1e-12:
            print("Pochodna równa 0 lub zbyt bliska 0 — metoda nie może kontynuować.")
            return None

        x_next = x_n - f_val / df_val

        print(f"Iteracja {i + 1}: x = {x_next}")

        if abs(x_next - x_n) < epsilon:
            print(f"\nPrzybliżony pierwiastek: {x_next}")
            return x_next

        x_n = x_next

    print("\nNie osiągnięto dokładności w zadanej liczbie iteracji.")
    return None


metoda_stycznych()