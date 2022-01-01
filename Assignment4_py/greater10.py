"""
File: greater10.py
------------------
assed a list of integers and returns a new list which contains only the numbers greater
than 10 from the original list passed in
"""


def greater_than_10(num_list):
    """
    This function is passed a list of integers (num_list) and should
    return a list containing only those numbers from num_list that
    have a value greater than 10.
    """
    greate10=[]
    if (len(num_list)==0):
        return greate10

    else:
        for s in num_list:
            if (s > 10):
                greate10.append(s)
        return greate10


def main():
    list1 = [20, 6, 12, -3, 14]
    result_list = greater_than_10(list1)
    print(result_list)      # should print [20, 12, 14]

    list2 = [16]
    result_list = greater_than_10(list2)
    print(result_list)      # should print [16]

    list3 = [1, 2, 3, 4]
    result_list = greater_than_10(list3)
    print(result_list)      # should print []

    list4 = []
    result_list = greater_than_10(list4)
    print(result_list)      # should print []


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
