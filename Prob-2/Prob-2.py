# Module 4
#   Programming Assignment 5
#       Prob-2.py

# <Garrett>

# Inputs: Total cost of transaction and amount tendered
# Process: Calculates change
# Outputs: Total change

# function definition
from math import *

def changeCalculator(totalPaid, totalDue):
    change = totalPaid - totalDue

    tenDollarAmount = change // 10
    tenDollarTotal = tenDollarAmount * 10
    fiveDollarAmount = (change - tenDollarTotal) // 5
    fiveDollarTotal = fiveDollarAmount * 5
    dollarAmount = (change - tenDollarTotal - fiveDollarTotal) // 1
    dollarTotal = dollarAmount * 1
    quarterAmount = (change - tenDollarTotal - fiveDollarTotal - dollarTotal) // .25
    quarterTotal = quarterAmount * .25
    dimeAmount = (change - tenDollarTotal - fiveDollarTotal - dollarTotal - quarterTotal) // .1
    dimeTotal = dimeAmount * .1
    nickelAmount = (change - tenDollarTotal - fiveDollarTotal - dollarTotal - quarterTotal - dimeTotal) // .05
    nickelTotal = nickelAmount * .05
    pennyAmount = (change - tenDollarTotal - fiveDollarTotal - dollarTotal - quarterTotal - nickelTotal) / .01
    
    output = ""
    if tenDollarAmount > 0:
        output += str(round(tenDollarAmount)) + " Ten Dollar Bill(s)\n"
    if fiveDollarAmount > 0:
        output += str(round(fiveDollarAmount)) + " Five Dollar Bill(s)\n"
    if dollarAmount > 0:
        output += str(round(dollarAmount)) + " Dollar Bill(s)\n"
    if quarterAmount > 0:
        output += str(round(quarterAmount)) + " Quarter(s)\n"
    if dimeAmount > 0:
        output += str(round(dimeAmount)) + " Dime(s)\n"
    if nickelAmount > 0: 
        output += str(round(nickelAmount)) + " Nickel(s)\n"
    if pennyAmount > 0:
        output += str(round(pennyAmount)) + " Penn(y/ies)\n"

    return output

# main function definition
def main():
    print()
    totalPaid, totalDue = eval(input("Enter a value for amount paid, then for cost, separated by a comma: "))
    print()
    print("Total change due: ")
    print(changeCalculator(totalPaid, totalDue))
    

    
    

main()
