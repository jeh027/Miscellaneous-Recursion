
def reverse_str(name):
    """
    This function takes in one argument: a string representing a
    name spelled backwards. The function then takes the string and 
    reverses it recursively so the string is in the correct order.
    At the end, the function will return the reverse order of
    the string.
    """

    if len(name) == 0:
        return ''
    if len(name) == 1:
        return name[0]
    else:
        return name[-1] + reverse_str(name[:-1])


def reverse_list(lst):
    """
    This function takes in one argument: a list of strings where 
    each word is reversed. The function iterates through the list
    and calls the helper function reverse_str to reverse the string 
    so it is in the correct order. If the function is given an empty 
    list, an empty list will be returned. 
    """

    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [reverse_str(lst[-1])]
    else:
        return [reverse_str(lst[0])] + reverse_list(lst[1:])



def remove_dragon(lst):
    """
    This function takes in one argument: a list of strings representing
    character names. The function will iterate through each string and
    remove any string that has "dragon" in it from the list no matter
    its case spelling. At the end, the function will return all the
    names that don't contain the substring "dragon" in it. 
    """

    if len(lst) == 0:
        return []
    if len(lst) == 1:
        if 'dragon' not in lst[0].lower():
            return [lst[0]]
        return []
    else:
        if 'dragon' not in lst[0].lower():
            return [lst[0]] + remove_dragon(lst[1:])
        else:
            return remove_dragon(lst[1:])


def sum_odd(lst):
    """
    This function takes in one argument: a list of integers. The
    function iterates through the list and only counts the odd
    numbers. At the end, the function returns the sum of all odd 
    numbers. If the function is given an empty list, an empty list 
    will be returned.
    """

    mod = 2

    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        if lst[0] % mod == 1:
            return lst[0]
        return 0
    else:
        if lst[0] % mod == 1:
            return lst[0] + sum_odd(lst[1:])
        else:
            return sum_odd(lst[1:])


def double_and_keep(amount, num_people):
    """
    This function takes in two arguments: a non-negative integer
    representing the starting amount of money, and another non
    negative integer representing the number of people you meet.
    For each person you meet, the function will double the amount
    and return the total amount of money received at the end.
    """
    double = 2

    if num_people == 0:
        return amount
    if num_people == 1:
        return amount * double
    else:
        return double_and_keep(amount * double, num_people - 1)


def place_matches(possible, wishes):
    """
    This function takes in two arguments: a list of strings representing
    places that you may potential visit and another list containing
    all the place you'd wish to visit. The function seeks to find 
    commonality among both these lists. At the end, the function 
    returns the number of places that you can and wish to visit as
    an integer.
    """

    if len(wishes) == 0:
        return 0
    if len(wishes) == 1:
        if wishes[0] in possible:
            return 1
        return 0
    else:
        if wishes[0] in possible:
            return 1 + place_matches(possible, wishes[1:])
        else:
            return 0 + place_matches(possible, wishes[1:])


def count_left(left, right):
    """
    This function takes in two arguments: a list of integers
    representing the benefits of going left and another list of 
    integers representing the benefits of going right. The function
    compares the corresponding list values and returns the amount of
    times going left is more benefical. If the left list value is 
    strictly greater than the right corresponding list value, or
    the index for the right list doesn't exist, a point is added to 
    the counter.
    """

    if len(left) == 0:
        return 0
    if len(left) == 1:
        if len(right) == 0:
            return 1
        if left[0] > right[0]:
            return 1
        if left[0] <= right[0]:
            return 0
    else:
        if len(right) == 0:
            return 1 + count_left(left[1:], right[1:])
        if left[0] > right[0]:
            return 1 + count_left(left[1:], right[1:])
        if left[0] <= right[0]:
            return 0 + count_left(left[1:], right[1:])


def generate_passcode(message):
    """
    This function takes in one argument: a string of words separated
    by exactly one space. The function takes the length of each word
    and concatenates them altogether into a string. At the end, the 
    function will return a string consisting of numbers. If the 
    function is given an empty string, an empty string will be 
    returned.
    """

    if len(message) == 0:
        return ''
    if message.find(' ') == -1:
        return str(len(message))
    else:
        return str(len(message[:message.find(' ')])) + generate_passcode(message[message.find(' ') + 1:])


def pebbles_to_friend(pebbles, num):
    """
    This function takes in two arguments: a list of integers
    representing pebble weights and a positive integer representing 
    the number of pebbles you want to give to each friends. The 
    function evenly divides the pebbles among all the friends and 
    the leftovers are ignored. At the end, the function returns a
    list integers representing the total weight you give to each 
    friend.
    """

    if len(pebbles) // num == 0:
        return []
    else:
        return [sum(pebbles[:num])] + pebbles_to_friend(pebbles[num:], num)