import code
def testupper_lower():
    actual = code.lower_upper("TESTMYCODE",1)
    assert actual, "testmycode"
    
    actual = code.lower_upper("calculator", 2)
    assert actual, "CALCULATOR"
    
def test_containsNumber():
    actual = code.contains_number("73Abdut77uial")
    assert actual
    
    actual = code.contains_number("abcDEsdf")
    assert not actual
    
def test_Valid_Number():
    actual = code.valid_number("897")
    assert actual
    
    actual = code.valid_number("asdaf")
    assert not actual
    
def test_remove_and_upper():
    
    actual = code.remove_and_upper("4ftern00n")
    assert "FTERNN" == actual, "Including digits and ch = 2"
    
    actual = code.remove_and_upper("assignment")
    assert "ASSIGNMENT" == actual, "Doesn't include digits and ch = 2"
    
def test_remove_and_lower():
    actual = code.remove_and_lower("BAA33LKD")
    assert 'baalkd' == actual, "Including digits"
        
    actual = code.remove_and_lower("STRUCTURE")
    assert "structure" == actual, "Doesn't include digits"
    
def test_meter_to_feet():
    actual = code.meters_to_feet(2)
    assert 6.562 == actual
    
def test_feet_to_meters():
    actual = code.feet_to_meters(13.124)
    assert 4 == actual
    
def test_cm_to_inches():
    actual = code.cm_to_inches(10)
    assert  3.937 == actual
    
def test_inches_to_cm():
    actual = code.inches_to_cm(4)
    assert 10.16 == actual
    
    
if __name__ == "__main__":
    testupper_lower()
    test_containsNumber()
    test_Valid_Number()
    test_remove_and_upper()
    test_remove_and_lower()
    test_meter_to_feet()
    test_feet_to_meters()
    test_cm_to_inches()
    test_inches_to_cm()