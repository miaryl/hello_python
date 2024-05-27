from prime_numbers import is_prime

def test_1_false():
    assert is_prime(1) == False

def test_2_true():
    assert is_prime(2) == True
