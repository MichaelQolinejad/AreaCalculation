print("**************************** ITC1070 Project ****************************")


# Function for calculation of the circle's area. Return a float number
def circle(radius):
    circleArea = radius * radius * 3.14
    return circleArea


# Function for calculation of the triangle's area. Return a float number
def triangle(base, height):
    triangleArea = (base * height) / 2
    return triangleArea


# Function for calculation of the parallelogram's area.Return a float number
def parallelogram(base, height):
    parallelogramArea = base * height
    return parallelogramArea


correction = True
# The loop is going on until we get the correct value, which is 1 , 2 or 3
while correction:
    try:
        # show the options to the user
        print("[1]Triangle\n[2]Parallelogram\n[3]Circle")
        # Input the number of the shape that user wants to find its area
        InputShape = input(
            "\nPlease choose the shape that you wish to find it's area from the above options(1, 2 or 3): ")
        # if you get correct input, break the loop and continue the program
        if InputShape == "1" or InputShape == "2" or InputShape == "3":
            break
        # If the input is not correct, ask until you get the correct input and then continue the program
        else:
            print("-------------------------------------------------------------------")
            print("Incorrect input, Please try again.(1, 2 or 3) \n")
    except ValueError:
        print("Your choice was not in correct format, Please try again.(1, 2 or 3)")

# If the choice is a circle
if InputShape == "3":
    print("***************************** CIRCLE'S AREA *****************************")
    # Stay in the loop until you get the correct value
    while True:
        try:
            # Ask for the input
            r = float(input("Enter the radius: "))
            # If the radius has positive value, do the calculation
            if r > 0:
                area = circle(r)
                # Print the circles area and then finish the program
                print("The area of the circle is {0}".format(area))
                break
            # If the value is negative or zero, ask for a new value
            else:
                print("Radius cannot be Zero or Negative!Please enter a positive integer number")
        # if the value doesn't have correct format,
        except ValueError:
            # print this,  ask again for the value
            print("Incorrect format!please enter a positive integer ")
            continue
# If the choice is Parallelogram
if InputShape == "2":
    print("***************************** PARALLELOGRAM'S AREA *****************************")
    # Stay in the loop until you get the correct value
    while True:
        try:
            # Ask for the base
            b = float(input("Enter the base: "))
        # if the base doesnt have correct format;
        except ValueError:
            # Print this,  ask again for the value
            print("Incorrect format!please enter a positive integer ")
            continue
        # If the Value is negative or zero, ask for inform user and ask for the correct value
        if b <= 0:
            # if the condition is true, ask for a new value
            print("the base value's cannot be Zero or Negative,Please try again")
            continue
        # If the value of the b is positive integer, then break the loop and continue the program
        else:
            break

    # Stay in the loop until you get the correct value
    while True:
        try:
            # Ask for the height
            h = float(input("Enter the height: "))
        # if the base doesnt have correct format;
        except ValueError:
            # Print this, ask again for the value
            print("Incorrect format!please enter a positive integer ")
            continue
        if h <= 0:
            # if the condition is true, ask for a new value
            print("the height value cannot be Zero or Negative,Please try again")
            continue
        # If the value of the h is positive integer, then break the loop and continue the program
        else:
            break

    # Calculation, pass the to saved value through the function and print the result
    area = parallelogram(b, h)
    print("The area of the parallelogram is {0}".format(area))

# If the shape is Triangle
if InputShape == "1":
    print("***************************** TRIANGLE'S AREA *****************************")
    # Ask for correct base
    while True:
        try:
            b = float(input("Enter the base: "))
        except ValueError:
            print("Incorrect format!please enter a positive integer ")
            continue
        # If the Value is negative, ask for inform user and ask for the correct value
        if b <= 0:
            # if the condition is true, ask for a new value
            print("the base values cannot be Zero or Negative,Please try again")
            continue
        # If the value of the b is positive integer, then break the loop and continue the program
        else:
            break

    # Stay in the loop until you get the correct value
    while True:
        try:
            # Ask for the height
            h = float(input("Enter the height: "))
        except ValueError:
            print("Incorrect format!please enter a positive integer ")
            continue
        if h <= 0:
            # if the condition is true, ask for a new value
            print("the height values cannot be Zero or Negative,Please try again")
            continue
        # If the value of the h is positive integer, then break the loop and continue the program
        else:
            break

    # Calculation
    area = triangle(b, h)
    print("The area of the triangle is {0}".format(area))
