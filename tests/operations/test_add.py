from calculator import add

""" Test Update """

def test_add():
    # Arrange
    first, second = 2, 3
    expected = 5
    
    # Act
    result = add(first, second)
    
    # Assert
    assert result == expected


def test_add_negative_numbers():
    # Arrange
    first, second = -2, -3
    expected = -5
    
    # Act
    result = add(first, second)
    
    # Assert
    assert result == expected


def test_add_zero():
    # Arrange
    first, second = 5, 0
    expected = 5
    
    # Act
    result = add(first, second)
    
    # Assert
    assert result == expected
