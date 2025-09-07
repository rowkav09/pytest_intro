import pytest

import grade_boundaries as gb

def test_calc_grade():
    assert gb.calc_grade(240, gb.default_boundaries) == 'A'
    assert gb.calc_grade(200, gb.default_boundaries) == 'B'

test_data = [
    (0, 'U'),
    (240, 'A'),
    (200, 'B')
]

@pytest.mark.parametrize("grade, expected", test_data)
def test_calc_grade_lots(grade, expected):
    assert gb.calc_grade(grade, gb.default_boundaries) == expected

def test_calc_grade_boundary():
    with pytest.raises(ValueError):
        gb.calc_grade(400, gb.default_boundaries)

    with pytest.raises(ValueError):
        gb.calc_grade(-1, gb.default_boundaries)

def test_calc_grade_type():
    with pytest.raises(TypeError):
        gb.calc_grade('A', gb.default_boundaries)
