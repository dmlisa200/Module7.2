"""
Program:  sort_and_search_list.py
author:  Lisa Kilmer
last modified:  June 21, 2020
This program has 2 functions.  the first is search_array that gives the index of the num in the
list that is provided.  It returns the index or if the num isn't found it returns -1.
The other function is sort_array that returns an ascending sorted list from the
provided list.
"""

my_list = [80, 9, 2, 7, 33, 115, 110]


def search_array(num):
    try:
        index = my_list.index(num)
        return index
    except ValueError:
        return int(-1)

def sort_array(list):
    new_list = sorted(list)
    return new_list


if __name__ == '__main__':
    print(search_array(3))
print(sort_array(my_list))

"""
    the return statement can contain an expression that returns a value or if there is no return 
    statement it will return none.  There may be a print expression that will return the value also
    then don't need return
    """