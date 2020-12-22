import sys

def ctof(c):
    return c*1.8 + 32

def ftoc(f):
    return (f-32)*5/9

def ctok(c):
    return c+273

def ktoc(k):
    return k-273

def ftok(f):
    return(ctok(ftoc(f)))

def ktof(k):
    return(ctof(ktoc(k)))

while(True):
    e = input("press y or Y to continue. press any other key to exit...")
    if e == 'y' or e == 'Y':
        print("Enter:\n1. C->F\n2. F->C\n3. C->K\n4. K->C\n5. F->K\n6. K->F")
        try:
            choice = int(input("Enter choice: "))
        except:
            print("invalid choice")
            continue

        if choice == 1:
            c = int(input("Enter temperature in celcius: "))
            print("Temperature in Farenheit: ", ctof(c))
        elif choice == 2:
            f = int(input("Enter temperature in farenheit: "))
            print("Temperature in Celcius: ", ftoc(f))
        elif choice == 3:
            c = int(input("Enter temperature in celcius: "))
            print("Temperature in kelvin: ", ctok(c))
        elif choice == 4:
            k = int(input("Enter temperature in kelvin: "))
            print("Temperature in celcius: ", ktoc(k))
        elif choice == 5:
            f = int(input("Enter temperature in farenheit: "))
            print("Temperature in Kelvin: ", ftok(f))
        elif choice == 6:
            k = int(input("Enter temperature in kelvin: "))
            print("Temperature in farenheit: ", ktof(k))
        else:
            print("invalid choice")
    else:
        print("Program ended")
        sys.exit()
    

    