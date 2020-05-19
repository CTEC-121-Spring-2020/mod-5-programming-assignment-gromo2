# Module 4
#   Programming Assignment 5
#       Prob-1.py

# <Garrett>

# Inputs: Number
# Process: Converts number to Roman Numeral
# Outputs: Roman Numeral

# function definition
def numberConvert(number):
    if number == 1:
        return "I"
    elif number == 2:
        return "II"
    elif number == 3:
        return "III"
    elif number == 4:
        return "IV"
    elif number == 5:
        return "V"
    elif number == 6:
        return "VI"
    elif number == 7:
        return "VII"
    elif number == 8:
        return "VIII"
    elif number == 9:
        return "IX"
    elif number == 10:
        return "X"
    elif number > 10:
        return "Error: Value is outside of expected range (1-10)."

    


# unit test function
def unitTest(): 
    print("\nUnit Tests")
    print()
    numberConvert(1)
    numberConvert(2)
    numberConvert(3)
    numberConvert(4)
    numberConvert(5)
    numberConvert(6)
    numberConvert(7)
    numberConvert(8)
    numberConvert(9)
    numberConvert(10)
    numberConvert(11)
    print()


    

def main():
    print("Main")    
    print() 
    number = int(input("Enter a number between 1 and 10: "))
    if number < 11:
        print("Input number", number, "translates to", numberConvert(number), "in Roman Numerals.")
    else:
        print(numberConvert(number))
    

    

unitTest()
main()