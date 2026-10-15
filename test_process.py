import pytest

from process import process


@pytest.mark.statement
@pytest.mark.parametrize("values, expected", [
    pytest.param([2], ["positivo", "par"], id="S1-A"),
])
def test_statement_coverage(values, expected):
    assert process(values) == expected


@pytest.mark.branch
@pytest.mark.parametrize("values, expected", [
    pytest.param([1, -2], ["positivo", "par"], id="D1-B-C"),
])
def test_branch_coverage(values, expected):
    assert process(values) == expected


@pytest.mark.path
@pytest.mark.parametrize("values, expected", [
    pytest.param([2, 2], ["positivo", "par", "positivo", "par"], id="P01-A-A"),
    pytest.param([2, 1], ["positivo", "par", "positivo"], id="P02-A-B"),
    pytest.param([2, -2], ["positivo", "par", "par"], id="P03-A-C"),
    pytest.param([2, -1], ["positivo", "par"], id="P04-A-D"),
    pytest.param([1, 2], ["positivo", "positivo", "par"], id="P05-B-A"),
    pytest.param([1, 1], ["positivo", "positivo"], id="P06-B-B"),
    pytest.param([1, -2], ["positivo", "par"], id="P07-B-C"),
    pytest.param([1, -1], ["positivo"], id="P08-B-D"),
    pytest.param([-2, 2], ["par", "positivo", "par"], id="P09-C-A"),
    pytest.param([-2, 1], ["par", "positivo"], id="P10-C-B"),
    pytest.param([-2, -2], ["par", "par"], id="P11-C-C"),
    pytest.param([-2, -1], ["par"], id="P12-C-D"),
    pytest.param([-1, 2], ["positivo", "par"], id="P13-D-A"),
    pytest.param([-1, 1], ["positivo"], id="P14-D-B"),
    pytest.param([-1, -2], ["par"], id="P15-D-C"),
    pytest.param([-1, -1], [], id="P16-D-D"),
])
def test_path_coverage(values, expected):
    assert process(values) == expected
