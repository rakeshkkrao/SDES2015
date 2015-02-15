from gcd import gcd

def test_gcd():
    assert gcd(48, 64) == 16
    assert gcd(44, 19) == 1
    assert gcd(-2, 5) == 0
    assert gcd(100,50) == 50
    assert gcd('a','b') == 0

if __name__ == '__main__':
    test_gcd()
