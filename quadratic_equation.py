from math import sqrt
import sys


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    else:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        if discriminant == 0:
            return root1, None
        else:
            return root1, root2


def input_abc():
    if len(sys.argv) <= 4:
        try:
            sys.argv[1], sys.argv[2], sys.argv[3]
            return "ok"
        except IndexError:
            print("Вы ввели меньше трех параметров для уравнения")
            return None
    else:
        print("Вы ввели больше трех параметров для уравнения")
        return None


def print_answer(root1, root2):
    if root1 is None:
        if root2 is None:
            print("Уравнение имеет комплексные корни")
        else:
            print("x1, x2 = ", root1)
    else:
        print("x1 =", root1, "  x2 =", root2)


if __name__ == "__main__":
    if input_abc() is not None:
        root1, root2 = get_roots(
            int(sys.argv[1]),
            int(sys.argv[2]),
            int(sys.argv[3])
        )
        print_answer(root1, root2)
