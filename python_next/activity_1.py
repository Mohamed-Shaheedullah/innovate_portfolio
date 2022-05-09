#
#

# define a variable to enable us to flag whether a value has been entered
entered = False

def check_int():
    # make global variable accessible
    global entered
    try:
        while not entered:
            my_var = input("please enter a number   >" )
            # check whether a valid entry
            if my_var == "" or not my_var.isnumeric():
                print("Please try again")
                check_int()
            else:
                # only set flag to true if there is a valid entry
                entered = True
                my_var = int(my_var)
                print("The data type of the entered number is shown below; ")
                print(type(my_var))
    except:
        print("Error***********************")

# call function
check_int()


