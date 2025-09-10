import pytest
from grade_boundaries import default_boundaries, calc_grade

def test_calc_grade():
    assert calc_grade(240, default_boundaries) == 'A'
    assert calc_grade(200, default_boundaries) == 'B'

test_data = [
    (x,y)
    for x,y in default_boundaries.items()
    if y is not 'Max'
]

def test_max_score():
    assert calc_grade(350, default_boundaries) == 'A*'

@pytest.mark.parametrize("grade, expected", test_data)
def test_calc_grade_lots(grade, expected):
    assert calc_grade(grade, default_boundaries) == expected

def test_calc_grade_boundary():
    with pytest.raises(ValueError):
        calc_grade(400, default_boundaries)

    with pytest.raises(ValueError):
        calc_grade(-1, default_boundaries)

def test_calc_grade_type():
    with pytest.raises(TypeError):
        calc_grade('A', default_boundaries)
