from mycounter import MyCounter


def test_initialization():
    # Test default initialization
    mc = MyCounter()
    assert mc.count == 0

    # Test initialization with a specific count value
    # Given
    mc = MyCounter(3)
    assert mc.count == 3


def test_set_count():
    mc = MyCounter()

    # Set count to a specific value and check
    mc.set_count(5)
    assert mc.count == 5

    # Set count to another value and check
    mc.set_count(10)
    assert mc.count == 10
