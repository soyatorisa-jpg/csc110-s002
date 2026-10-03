# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """Read two integers and return them as a pair
    Prompt the user to enter two different integers
    return: a pair of integers (int, int).
    """    
    x = int(input("give me x: "))
    y = int(input("give me y: "))
    
    return x, y
    
# the return shown below is a placeholder to make sure this runs
# return: a pair of integers (int, int).
    

# This calls the function and runs it right now




# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    """Calculate and print the parts of the operation on the two input variables and then return it
"""
    # the pass shown below is a placeholder to make sure this runs
    # equation to use is (a * b) / (a + b)
    a = int(input("give me a: "))
    b = int(input("give me b: "))
    
#calculate the numerator first
    mult_result = a * b 
    print(f"mult_result: {mult_result}")
    
#Calculate the denominator
    add_result = a + b
    print(f"add_result: {add_result}")

# Return the results
    return mult_result / add_result

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    """Print the inputs and the results of multadd in order."""
    # the pass shown below is a placeholder to make sure this runs
    print("*" * 16)
    print("RESULTS:")
    print(f"first number: {a}")
    print(f"second number: {b}")
    print(f"multadd result: {ab_multadd}")
    print("=" * 16)
    pass

def main ():
    """Main function to run the tasls."""
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
    x, y = read_two_ints()

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd
    xy_multadd = compute_multadd(x, y)

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;
    print_fancy(x, y, xy_multadd)


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
