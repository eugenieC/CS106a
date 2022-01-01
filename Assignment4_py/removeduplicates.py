"""
File: removeduplicates.py
-------------------------
Reading values into a list and removing duplicates
"""


def read_list():
    """
    This function should ask the user for a series of integer values
    (until the user enters 0 to stop) and store all those values in a
    list.  That list should then be returned by this function.
    """
    italics = '\033[3m'
    plain = '\033[0m'

    number_list=[]
    while True:
        input_value=input(plain+"Enter value (0 to stop):"+italics)
        if input_value=="0":
            break
        number_list.append(int(input_value))
    print(plain+"")
    return number_list
    

def remove_duplicates(num_list):
    num_list
    no_dup=[]
    for x in num_list:
        if x not in no_dup:
            no_dup.append(x)
    return no_dup


def main():
    num_list = read_list()
    print("Original list entered by user: ")
    print(num_list)

    no_duplicates = remove_duplicates(num_list)
    print("List with duplicates removed: ")
    print(no_duplicates)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
