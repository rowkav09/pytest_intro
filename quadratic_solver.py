import math

def solve_quadratic(a: int, b: int, c: int) -> tuple[float, float]:
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("coefficients must be numbers")

    if a == 0:
        raise ValueError("a must not be 0 for a quadratic")

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        raise ValueError("no real solutions")

    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)

    return (root1, root2)
