# Desafio 003:
# How Many Solutions Does This Quadratic Have?
# Note: a != 0
# ----------------------------------------------------------------------------


def solucoes(a: float != 0, b: float, c: float) -> int:
    Delta = (b ** 2) - 4 * a * c
    if Delta > 0:
        return 2
    elif Delta < 0:
        return 0
    return 1


if __name__ == '__main__':
    print(solucoes(1, 4, 8))
