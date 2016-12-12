from Math import Math

def test_add():
    assert Math.add(10, 4) == 14

def test_subtract():
    assert Math.subtract(10, 4) == 6

def test_multiply():
    assert Math.multiply(10, 3) == 30

def test_divide():
    assert Math.divide(100, 2) == 50
