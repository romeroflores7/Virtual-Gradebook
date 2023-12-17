def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    """
    lines = "=========================="
    title = "What would you like to do?"
    print(lines)
    print(title)

    for letter, value in menu.items():
        print(f'{letter} - {value}')

    print(lines)


def get_grades(info_list):
    '''Takes in one parameter then goes through the info_list then makes a new list with only     the grades'''
    counter = 0
    gradelist = []
    for category in enumerate(info_list):
        gradelist.append(info_list[counter]["grades"])
        counter += 1
    return gradelist


def get_total_grade(info_list, show_steps=True):
    '''Gets the total grade
    parameter infolist
    gets the average '''

    counter = 0
    avg_sum = 0
    only_grades = get_grades(info_list)
    avg_grades = get_list_avg(only_grades)

    for pos, category in enumerate(info_list):
        try:

            x = (avg_grades[pos]) * (0.01 * (info_list[pos]["weight"]))
            avg_sum += x

        except ZeroDivisionError:
            avg_sum += 0

    return avg_sum


def get_list_avg(list):
    '''gets the list by finding the sum of them and then adding it to a list'''
    counter = 0
    list_avg = []
    for l in list:
        try:

            x = sum(list[counter])
            xx = x / len(list[counter])
            list_avg.append(xx)
            counter += 1
        except ZeroDivisionError:
            x = 0
            list_avg.append(x)

    return list_avg


def get_selection(action, suboptions):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
            The keys are assumed to be in upper-case.

    The function displays a submenu for the user to choose from.
    Asks for user to select an option using the input() function.
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection as an upper-case string
            (should be a valid key in the suboptions)
    """
    selection = None
    while selection not in suboptions:
        print(f"What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        selection = input("::: Enter your selection\n> ")
        selection = selection.upper()  # to allow us to input lower- or upper-case letters
    print(f"You selected {selection} to",
          f"{action.lower()} {suboptions[selection].lower()}.")
    return selection


def print_grade_info(info_list, show_grades=True):
    """
    param: info_list - a list that contains dictionaries
    param: show_grades - a Boolean flag (True by default)
            controls whether the function outputs the grades
            for each assignment; if set to False, only displays
            category information
    Each dictionary in the info_list is supposed to have
    the following string keys:
    """

    for n, cat in enumerate(info_list):

        if show_grades == False:
            print(f'{n + 1} - {info_list[n]["category"]} ({info_list[n]["weight"]}%)')
        else:
            print(f'{n + 1} - {info_list[n]["category"]} ({info_list[n]["weight"]}%)')
            print(f'{info_list[n]["grades"]}')

            # print(f'{n} - {cat}')


def is_num(val):
    '''The function checks if `val` is a string;
    returns False if `val` is not a string.
    Otherwise, returns True if the string `val`
    contains a valid integer or a float.
    Returns False otherwise.'''

    if type(val) != str:
        return False
    for i in val:
        if i.isalpha() == True:
            return False
    if val.count('.') > 1:
        return False

    if val.isdigit() == True or type(float(val)) == float:
        return True
    else:
        return False


def is_num_str_list(list):
    '''Checks if the nums in list       are nums with the parameter of      list and checks if the numbers      are integers '''
    if list == []:
        return False
    for i in list:
        if type(i) != str:
            return False
        if is_num(i) == False:
            return False
    return True


def create_category(info_str):
    '''takes an info str as a paramter and then splits the input and puts them into lists and checks to see if it meets the requirements to be considred true'''
    createlist = []
    name = info_str.split()

    for i in name:
        createlist.append(i)

    if len(createlist) != 2:
        return -2
    if len(createlist[0]) < 2 or ',' in createlist[0]:
        return -1
    if is_num(createlist[1]) == False:
        return 0

    newdict = {
        "category": createlist[0],
        "weight": float(createlist[1]),
        "grades": []}

    return newdict


def is_valid_index(idx, in_list, start_idx=0):
    '''is valid index checks the idx and subtracts the start idx and in_list to see if it has a valid range or out of range'''

    if is_num(idx) == True:
        if int(idx) >= 0:
            try:
                in_list[int(idx) - start_idx]
                return True

            except IndexError:
                return False


    else:
        return False


def update_category(info_list, idx, info_str):
    '''takes an info str as a parameter and then splits it and puts them into lists and see if it is considered true'''
    result = create_category(info_str)
    info_list[idx] = result
    return info_list[idx]


def delete_item(in_list, idx, start_idx=1):
    '''takes in a list an idx of category to get rid of, then returns the deleted item'''
    if int(idx) <= 0:
        return -1
    if len(in_list) == 0:
        return 0
    if type(idx) != str:
        return None
    if is_valid_index(idx, in_list, start_idx=0) == False:
        return -1

    item = in_list[int(idx) - start_idx]
    in_list.remove(item)
    return item
