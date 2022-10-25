# Parameter in function definition AND Arguments in function call
# positional parameters: in function call arguments are loaded into function parameters in an order / matching by order
# keyword parameters (w/o defaults): In function call arguments given with key, loads into function parameters by matching key instead of order
# keyword parameters (w defaults): In function call arguments can be skipped if default value is given in function parameters
# optional positional arguments: *opt_args > any number of arguments pass as tuple
# optional arguments: **opt_args > any no of keyword arguments pass as dictionary (key/value pair)

## > Note: Order of arguments/parameters in function must be as follows:
## > (positional arguments, *opt_positional_args, keyword arguments w default, **opt_kwargs)

def greetings_1(fname, lname):
    print(f"Hello {fname} {lname}")

greetings_1("Shamayla", "Shahzadi")

def greetings_2(fname, lname):
    print(f"Hello {fname} {lname}")

greetings_2(lname="Shahzadi", fname="Shamayla")

def greetings_3(fname, lname=""):
    print(f"Hello {fname} {lname}")

greetings_3("Shamayla")

def greetings_4(fname, lname, *args, flatter="The beautiful", **kwargs):
    print(f"Hello {fname} {lname} {flatter}")
    print(f"Your list of friends are {args}")
    print("Your details are:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greetings_4("Shamayla", "Shahzadi", "Saira", "Anoshia", "Zoya", height="5 4", age="34", fav_color="Purple")


