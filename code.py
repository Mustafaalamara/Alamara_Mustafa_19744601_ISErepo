def lower_upper(string, ch):
    #print('''1- For lowercase
#2- For uppercase
#''')
    #ch = int(input("Choose: "))
    if ch == 1:
        n = string.lower()
    elif ch == 2:
        n = string.upper()
    print(n)
    return n
#convert_to_upper(input("Enter: "))

def containsNumber(string):
    for a in string:
        if a.isdigit():
            a = True
            print("It does contain numbers")
        else:
            a = False
            print("It doesn't contain numbers")
    return a
#print(containsNumber(input("ghh: ")))

def valid_number(string):
    for a in string:
        if a.isnumeric():
            return True
    return False
#print(valid_number(input("Num: ")))


def remove_and_change(string, ch):
    for a in string:
        if (a.isdigit()) == True:
            string = ''.join((x for x in string if not x.isdigit()))   
    if ch == 1:
            ns = string.lower()
    elif ch == 2:
            ns = string.upper()
    print(ns) 
#remove_and_change("KASDas334JA", 1)

def meters_to_feet(meters):
    return meters * 3.281

def feet_to_meters(feet):
    return feet / 3.281

def cm_to_inches(cm):
    return cm * 0.3937

def inches_to_cm(inches):
    return inches * 2.54
    
