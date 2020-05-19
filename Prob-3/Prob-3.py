# Module 4
#   Programming Assignment 5
#       Prob-3.py

# <Garrett>

# Inputs: Total area (square feet), cost of paint

from math import *

# function definition
def paintJob(totalArea, paintCost):
    hours = 8 * (totalArea / 112)
    totalPaint = ceil(totalArea / 112)
    laborCost = 35 * hours
    totalPaintCost = totalPaint * paintCost
    totalCost = laborCost + totalPaintCost + 99
    output = "Job Summary: \n"
    output += "Gallons of Paint: " + str(totalPaint) + "\n"
    output += "Estimated Hours of Labor: " + str(round(hours)) + "\n"
    output += "Cost of Paint: $" + str(totalPaintCost) + "\n"
    output += "Labor Cost: $" + str(laborCost) + "\n"
    output += "Total Estimate: $" + str(totalCost)
    return output

# main function definition
def main():
    print()
    totalArea, paintCost = eval(input("Enter the total area of the job (in square feet, as a number only), and the total cost of paint per gallon, separated by commas: "))
    print(paintJob(totalArea, paintCost))
main()
