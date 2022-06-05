def lower_upper(string, ch):
    if ch == 1:
        n = string.lower()
    elif ch == 2:
        n = string.upper()
    return n

def contains_number(string):
    b = False
    for a in string:
        if a.isdigit():
            b = True
    return b
    
def valid_number(string):
    b = False
    for a in string:
        if a.isnumeric():
            b = True
    return b
    
def remove_and_upper(string):
    for a in string:
        if (a.isdigit()) == True:
            string = ''.join((x for x in string if not x.isdigit()))
    return string.upper()

def remove_and_lower(string):
    for a in string:
        if (a.isdigit()) == True:
            string = ''.join((x for x in string if not x.isdigit()))
    return string.lower()

def meters_to_feet(meters):
    return meters * 3.281

def feet_to_meters(feet):
    return feet / 3.281

def cm_to_inches(cm):
    return cm * 0.3937

def inches_to_cm(inches):
    return inches * 2.54
    
