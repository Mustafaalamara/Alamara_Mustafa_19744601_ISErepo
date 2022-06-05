# ISE FINAL ASSESSMENT

### MUSTAFA ALAMARA
### 19744601
##### THURSDAY 10 AM - 312.221

---
### INTRODUCTION
Based on the concepts that we have learned in the past weeks this semester we had to build a program with some functionalities. Along with the code for the program test designs including both black box and white box testing approaches are to be implemented in this assignment. The functions that are to be implemented will include all of category a which includes changing to upper case or lower case and removing numbers. It will also include functions to convert from one length unit to another (from meters to feet and vice versa and from centimetres to inches and vice versa).

### MODULE DESCRIPTION
The code of the program includes many functions and modules. The modules included in the code:
* Lower_Upper
* Contains_Number
* Valid_number
* Remove_and_upper
* Remove_and_lower
* Meters_to_feet
* Feet_to_meters
* Cm_to_inches
* Inches_to_cm


The lower_upper function was chosen to change the string provided to either entirely upper case or ultimately lower case. The user chooses whether they want to convert the string to upper case or lower case. They can pick which one when they put in the string.

The contains_number function is made to take in the string by the user and check if the string includes any digit in it. When the string has input, it will go through the string, and if there is a digit in the string, it will return True, and if it does not find a digit in the string, it will return a False.

The valid_number function is made to take in the string by the user and check if the string includes valid numbers. So when the user gives the string input, it will go through the string, and if there is a valid number in the string, it will return True, and if it does not find a valid number in the string, it will return a False.

The remove_and_upper function is made so that the user can input a string that can include numbers or digits in it. If the program finds digits, it will remove them from the string and then change the whole string to all upper case and print it out.

The remove_and_lower function is made so that the user can input a string that can include numbers or digits in it. If the program finds digits, it will remove them from the string and then change the whole string to all lower case and print it out.

The meters_to_feet function is a length unit convertor. The function takes in the value given by the user. The taken-in value is in meters, and the function through calculations changes it into feet. The function output the value with a new value with a different length unit. 

The feet_to_meter function does what the meter_to_feet function does but in the opposite direction. It is also a length unit convertor. The function takes in the value given by the user. The taken-in value is in feet, and the function through calculations changes it into meters. The function output the value with a new value with a different length unit. 

The cm_to_inches function is a length unit convertor. The function takes in the value given by the user. The taken-in value is in centimeters, and the function through calculations changes it into inches. The function output the value with a new value with a different length unit. 

The inches_to_cm function also does what cm_to_inches does but in the opposite direction. It is a length unit convertor. The function takes in the value given by the user. The taken-in value is in centimeters, and the function through calculations changes it into inches. The function output the value with a new value with a different length unit.

### MODULARITY
To run the code, the user will need the correct commands to work properly. For example, for the lower_upper function, ,the user would need to give it two commands to run the code correctly. The first command would be the string the user wants to input and whether they want to change the entire string into upper case (2) or lower case (1). For example, the user will call the function and input ("Dark Knight" , 2).
The result would be DARK KNIGHT, as 2 changes the entire string into upper case and 1 changes the string into all lower case.

The contains_number function will need a string input. The user can add any string they want. The code will check if it contains any digits and return a result. For example, if the input string is "IUAS4" the result will be True.

The valid_number function carries the same format and is used the same way as the contains_number function. This function scans the code for any valid number, and if it finds any, it will return a True, otherwise a False.

The remove_and_upper function takes in a string provided by the user. The commands given to do work correctly only include any string the user wants to input. For example,, if the user inputs "4ftern00n" the function will remove any digits, change all letters to the upper case, and return an "FTERNN".

The remove_and_lower function works the same way as the remove_and_upper function and takes in the same command. It takes in a string provided by the user. The commands given to do work correctly only include any string the user wants to input. For example,, if the user inputs "CHA5IB" the function will remove any digits, change all letters to lower case, and return a "chaib".

The meter_to_feet function will need the user to input a number they want to convert from meters to feet. The input is very simple. For example, if the user inputs 1 in meters, the function will do some calculations and convert it to 3.281 in feet and return the result.

The feet_to_meter function follows the same concept as the meter_to_feet. The user must input a number that they want to be converted from feet to meters. The input is very simple. For example, if the user inputs 3.281 in feet, the function will do some calculations and convert it to 1 in meters and return the result.

The cm_to_inches function will need the user to input a number that they want to be converted from centimeters to inches. The input is very simple. For example, if the user inputs 1 in centimeters, the function will do some calculations and convert it to 0.3937 in inches and return the result.

The inches_to_cm function follows the same concept as the cm_to_inches. The function will need the user to input a number that they want to convert from meters to feet. The input is very simple. For example, if the user inputs 1 in inches, the function will do some calculations and convert it to 2.54 in centimeters and return the result.

Checklist for the code:
* Low coupling
* Code Complexity
* Global variables
* Clean and clear code
* High cohesion

When reviewing the checklist on the code, the code follows most of the points in the checklist. The code has low coupling, and few functions affect other functions. The code complexity is low, and the code is relatively clean and clear. The straightforwardness of the code makes it simple to change anything if needed or if there is an error. It is also easy to read and understand by most people who have experience with Python. There is low cohesion in the code, and every function does its own thing without referring to another function.
The code doesn't include global variables as global variables increase couplings and it would not be desired for the code.

### BLACK-BOX TEST CASES
Two test cases were created for the same purpose of testing the code for any errors. Both test cases are included below. Both test cases were applied to the code, and both returned with no errors. The test cases were based on the expected results from each function. If the output expected was either True or False, the approach differed from the functions that would output results in numbers, digits, or a string. No assumptions were made, and only the outputs of the functions and the way they were written decided on how they should be tested.
#### Testt.py
```python
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
```
#### testMyCode.py
```python
import code
def testupper_lower():
    actual = code.lower_upper("TESTMYCODE",1)
    assert actual, "testmycode"
    
    actual = code.lower_upper("alamara", 2)
    assert actual, "CALCULATOR"
    
def test_containsNumber():
    actual = code.contains_number("19744601")
    assert actual
    
    actual = code.contains_number("Mustafa Alamara")
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
        
    actual = code.remove_and_lower("SPIDERMAN")
    assert "spiderman" == actual, "Doesn't include digits"
    
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
```

| Module Name | BB test design | WB test design | EP test code (Implemented/run) | WB testing | Errors |
| ----------- | -------------- | -------------- | ------------------------------ | ---------- | ------ |
| lower_upper | Done           | Not Done       | Implemented and run            | NO         | None   |
| valid_number| Done           | Not Done       | Implemented and run            | NO         | None   |
| remove_and_upper | Done      | Not Done       | Implemented and run            | NO         | None   |
| remove_and_lower | Done      | Not Done       | Implemented and run            | NO         | None   |
| meter_to_feet | Done         | Not Done       | Implemented and run            | NO         | None   |
| feet_to_meter  | Done        | Not Done       | Implemented and run            | NO         | None   |
| cm_to_inches | Done          | Not Done       | Implemented and run            | NO         | None   |
| inches_to_cm  | Done         | Not Done       | Implemented and run            | NO         | None   |

![Screenshot](SC.png)

![Screenshot2](SC2.png)

The results of the testing was very positive on both test cases. White

### ETHICS AND PROFESSIONALISM

Ethics and professionalism are crucial for any case and software developer. The codes they write and the programs they design have to consider ethics and professionalism and think deeply about it, and the code considers it. One aspect of ethics and professionalism is the primacy of the public interest. When designing the code, this has to be valued and identifying how it can potentially impact all the parties involved and their interests. If the code written does not comply with the interests of the people involved, it can be unethical and unprofessional as it wastes the time of all the parties involved if it does not comply with their needs. The code should strive to help enhance the quality of life for the users and simple use. The code's purpose is so that the users can do what they want without it being complex or time-wasting. The code does so and therefore follows ethics and professionalism to enhance the quality of life aspect.
The code has to follow honesty and not breach the specific trust of the parties involved. Plagiarising someone else's code goes against honesty, and it can be an attempt to enhance the developer's reputation at the expense of another person's reputation and hard work. The code does not go against honesty or plagiarise someone else's work or hurt them.
Professional development is also included in the code as through it, and it helps upgrade the knowledge and skills of the creator and supports education and training. Professionalism was applied in the code by taking a calm, objective, informed, and knowledgeable stance on the work and completing it with enthusiasm and engagement. 

Some suggestiongs to avoid ethical and professional issues in the software proposed are:
* Accepting the responsibility of the software proposed and not misrepresenting skills or knowledge

* Give credit where credit is due and not mislead the users about the suitability of the software or service

### DISCUSSION

Reflecting on my work, there were many things that I would have liked to change to improve my work. I would have loved to start this assignment earlier to get more help from the tutors and understand some concepts better. Starting earlier would've given me more time to do the assignment, but I had to do other assignments for different units. Time management would be key to improving my work and presenting it in a better way. 
I enjoyed working on this assignment and enjoyed the unit. I also learned a lot from this unit and will hopefully be using this knowledge learned from this unit for the future of my student and work life.
