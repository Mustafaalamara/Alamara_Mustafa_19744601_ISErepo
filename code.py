def lower_upper(string):
    print('''1- For lowercase
2- For uppercase
''')
    ch = int(input("Choose: "))
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

def remove_and_change(string):
    for a in string:
        if (a.isdigit()) == True:
            newstring = ''.join((x for x in string if not x.isdigit()))
    #return string.upper()
    print('''1- For lowercase
2- For uppercase
''')
    ch = int(input("Choose: "))    
    if ch == 1:
        ns = newstring.lower()
    elif ch == 2:
        ns = newstring.upper()
    print(newstring)
    return ns
#print(remove_and_change(input()))

'''def meters_to_feet(meters):
    return meters * 3.281

def feet_to_meters(feet):
    return feet / 3.281

def cm_to_inches(cm):
    return cm * 0.3937

def inches_to_cm(inches):
    return inches * 2.54'''
    
def meter_feet():
    print('''Which conversion do you want?
1- Meter to feet
2- Feet to meter
''')
    mi = int(input("Choose: "))
    if mi == 1:
        meter = float(input("Enter the length in meters: "))
        feet = float()
        feet = 3.281 * meter
        print("The length in feet = ", round(feet,2))
    elif mi == 2:
        meter = float()
        feet = float(input("Enter the length in feet: "))
        meter = feet / 3.281
        print("The length in meters = ", round(meter,2))

meter_feet()

def cm_inches():
    print('''Which conversion do you want?
3- Centimetres to inches
4- Iches to Centimetres
''')
    mi = int(input("Choose: "))
    if mi == 3:
        centimetre = int(input("Enter the length in centimetres: "))
        inches = int()
        inches = centimetre * 0.3937
        print("The length in inches = ", round(inches,2))

    if mi == 4:
        inches = int(input("Enter the length in inches: "))
        centimetre = int()
        centimetre = inches * 2.54
        print("The length in centimetres = ", round(centimetre,2))
        
cm_inches()