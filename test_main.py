from main import add, subtract


def test_add():
    result = add(2, 3)
    assert result == 5, f"Expected 5, but got {result}"


def test_subtract():
    result = subtract(5, 3)
    assert result == 2, f"Expected 2, but got {result}"
