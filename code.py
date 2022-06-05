def convert_to_upper(string):
    print(string.upper())
#convert_to_upper(input("Enter: "))

def containsNumber(string):
    for a in string:
      if a.isdigit():
        return True
    return False
#print(containsNumber(input("ghh: ")))

def valid_number(string):
    for a in string:
        if a.isnumeric():
            return True
    return False
#print(valid_number(input("Num: ")))

def remove_and_change(string):
    for a in string:
        if (a.isdigit()) == True:
            string = ''.join((x for x in string if not x.isdigit()))
    return string.upper()
    
#print(remove_and_change(input()))

def meters_to_feet(meters):
    return meters * 3.281

def feet_to_meters(feet):
    return feet / 3.281

def cm_to_inches(cm):
    return cm * 0.3937

def inches_to_cm(inches):
    return inches * 2.54