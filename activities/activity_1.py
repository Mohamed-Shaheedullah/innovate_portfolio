
# create global variables
my_welcome = "Welcome to Code Nation "
length_of_welcome = len(my_welcome)

# create function to check even or odd and print message
def check_even():
    if length_of_welcome%2==0:
        print(f"\"{my_welcome}\" is {length_of_welcome} letters long")
    else:
        print(f"\"{my_welcome}\" is {length_of_welcome} letters long, an odd number")

# call function
check_even()

