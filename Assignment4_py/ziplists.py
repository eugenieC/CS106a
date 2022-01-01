"""
File: ziplists.py
-----------------
passed two lists of strings (list1 and list2), where you can assume that both
lists both have the same length (number of elements). The function should return a new
list that "zips" together the two lists passed in. 
"""


def zip2lists(list1, list2):
    ziplist=[]
    for i in range(0,len(list1)):
        ziplist.append([list1[i],list2[i]])
    return ziplist

def main():
    result_list = zip2lists(['a', 'b', 'c'], ['d', 'e', 'f'])
    print(result_list)      # should print [['a', 'd'], ['b', 'e'], ['c', 'f']]

    result_list = zip2lists([], [])
    print(result_list)      # should print [['a', 'd'], ['b', 'e'], ['c', 'f']]

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
