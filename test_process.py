import pytest

from process import process


@pytest.mark.statement
@pytest.mark.parametrize("values, expected", [
    pytest.param([2], ["positivo", "par"], id="S1-A"),
])
def test_statement_coverage(values, expected):
    assert process(values) == expected
