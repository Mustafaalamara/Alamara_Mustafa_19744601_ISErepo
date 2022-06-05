import code
import unittest
class MyTest(unittest.TestCase):
    def testupper_lower(self):
        actual = code.lower_upper("TESTMYCODE",1)
        self.assertTrue(actual)
        
        actual = code.lower_upper("alamara", 2)
        self.assertTrue(actual)
 
    def test_containsNumber(self):
        actual = code.contains_number("19744601")
        self.assertTrue(actual)
        
        actual = code.contains_number("Mustafa Alamara")
        self.assertFalse(actual)
        
    def test_Valid_Number(self):
        actual = code.valid_number("897")
        self.assertTrue(actual)

        actual = code.valid_number("asdaf")
        self.assertFalse(actual)

    def test_remove_and_upper(self):
        self.assertEqual("FTERNN", code.remove_and_upper("4ftern00n") )
        self.assertEqual("ASSIGNMENT", code.remove_and_upper("assignment") )

    def test_remove_and_lower(self):
        self.assertEqual("baalkd", code.remove_and_lower("BAA33LKD"))
        self.assertEqual("spiderman", code.remove_and_lower("SPIDERMAN"))

    def test_meter_to_feet(self):
        self.assertEqual(6.562, code.meters_to_feet(2))
        
    def test_feet_to_meters(self):
        self.assertEqual(4, code.feet_to_meters(13.124))
        
    def test_cm_to_inches(self):
        self.assertEqual(3.937, code.cm_to_inches(10))
        
    def test_inches_to_cm(self):
        self.assertEqual(10.16, code.inches_to_cm(4))
    
