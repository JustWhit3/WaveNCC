# System libraries
from math import sin

# My libraries
import utils
import functions

def func(x):
    return pow(x,2)

#################################################
#     Main program
#################################################

# Main function
def main():
    formula = "func(x)*sin(x)*x**2"
    code = parser.expr(formula).compile()
    x = 10
    print(eval(code))

# Main running
if __name__ == "__main__":
    main()