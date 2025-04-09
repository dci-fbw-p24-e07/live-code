from main import add

# Add
def test_add_returns_integer():
    result = add(5, 10)
    assert isinstance(result, int), "Result not an integer"
    
def test_add_returns_correct_result():
    result = add(16, 10)
    assert (result == 26), "The result from add does not match"
    
def test_add_returns_negative_from_negative_input():
    pass

# Multiply

# Divide

# Subtract

test_add_returns_integer()
test_add_returns_correct_result()