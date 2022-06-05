import code
def testconversion():
    actual = code.cm_inches(1, 10)
    assert 13 == actual
    
    
if __name__ == "__main__":
    testconversion()