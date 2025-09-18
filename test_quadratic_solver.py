import pytest
from quadratic_solver import solve_quadratic

def test_basic_quadratic():
    # x^2 - 3x + 2 = 0 → roots 1 and 2
    assert solve_quadratic(1, -3, 2) == (2.0, 1.0)

def test_double_root():
    # x^2 - 2x + 1 = 0 → root 1 twice
    assert solve_quadratic(1, -2, 1) == (1.0, 1.0)

def test_invalid_a():
    with pytest.raises(ValueError):
        solve_quadratic(0, 2, 1)

def test_non_real_roots():
    with pytest.raises(ValueError):
        solve_quadratic(1, 0, 1)

def test_type_error():
    with pytest.raises(TypeError):
        solve_quadratic("a", 2, 1)
