from functions import *


def add_helper():
    continue_action = 'y'  # a Boolean flag for running the loop
    while continue_action == 'y':
        subopt = get_selection(the_menu[opt], submenu)
        if subopt == 'C':
            print("::: Enter the category name and percentage (e.g., Quiz 15)")
            ctg_info = input("> ")
            new_ctg = create_category(ctg_info)
            if type(new_ctg) == dict:
                all_grades.append(new_ctg)
                print(f"Successfully added |{ctg_info}|")
            else:  # returned an error
                print("WARNING: invalid category information!")
                print(f"Category information |{ctg_info}| was not added.")  # see the "Adding a new category" section
        elif subopt == 'G':
            print("To which category would you like to add new grades?")
            print_grade_info(all_grades, show_grades=False)
            print("::: Enter the number corresponding to the category.")
            user_option = input("> ")
            if is_valid_index(user_option, all_grades, 1) == True:
                ctg_idx = int(user_option) - 1
                category = all_grades[ctg_idx]["category"]

                print(f"Adding grades to {category}")
                print(f"{all_grades[ctg_idx]}")
                print("::: Enter the numeric grades separated by spaces")
                grade_info = input("> ")
                grade_list = grade_info.split()

                if is_num_str_list(grade_list):

                    all_grades[ctg_idx]["grades"] += grade_list
                    print(f"Success!")
                    print(f"{all_grades[ctg_idx]}")
                else:  # is_num_str_list() returned False
                    print("WARNING: invalid grade information!")
                    print(f"The grade data |{grade_info}| was not added.")
            else:  # is_valid_index() returned False
                print(
                    f"WARNING: |{user_option}| is an invalid category number!")  # see the "Adding a new grade" section
        print("::: Would you like to enter another item?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()


def update_helper():
    continue_action = 'y'
    while continue_action == 'y':
        print("Which category would you like to update?")
        print_grade_info(all_grades, show_grades=False)
        print("::: Enter the number corresponding to the category.")
        user_option = input("> ")
        if is_valid_index(user_option, all_grades, 1):  # check that the user_option is a valid index
            ctg_idx = int(user_option) - 1

            # Save the current category name and weight
            category = all_grades[ctg_idx]["category"]
            weight = all_grades[ctg_idx]["weight"]

            print(f"Updating category {category} ({weight}%)")
            print("::: Enter the new category name and percentage (e.g., Quiz 15)")
            ctg_info = input("> ")
            result = update_category(all_grades, ctg_idx, ctg_info)
            if type(result) == dict:
                print("Success!")
                print(f"Updated {category} ({weight}%)",
                      f"to {all_grades[ctg_idx]['category']} ({all_grades[ctg_idx]['weight']}%)")
            else:  # update_category() returned an error
                print("WARNING: invalid category information!")
                print(f"Category information |{ctg_info}| was not added.")
        else:  # is_valid_index() returned False
            print(f"WARNING: |{user_option}| is an invalid category number!")

        print("::: Would you like to update another category?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()


def delete_helper():
    continue_action = 'y'
    while continue_action == 'y':
        print("Which category would you like to delete?")
        print_grade_info(all_grades, show_grades=False)
        print("::: Enter the number corresponding to the category.")
        user_option = input("> ")
        result = delete_item(all_grades, user_option, 1)
        if type(result) == dict:
            print("Success!")
            # Get the deleted category name and weight
            category = result["category"]
            weight = result["weight"]
            print(f"Deleted {category} ({weight}%)")
        elif result == 0:  # delete_item() returned an error
            print("WARNING: there is nothing to delete.")
        elif result == -1:  # is_valid_index() returned False
            print(f"WARNING: |{user_option}| is an invalid category number!")

        print("::: Would you like to delete another category?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()


the_menu = {
    "T": "Total grade",
    "L": "List",
    "A": "Add",
    "U": "Update",
    "D": "Delete",
    "S": "Save the data",
    "R": "Restore data from file",
    "Q": "Quit this program"
}
submenu = {
    "C": "Categories",
    "G": "Grades"
}

opt = None

all_grades = [
    {"category": "PA",
     "weight": 5,
     "grades": [100.0, 100.0, 100.0, 100.0, 100.0, 0.0, 95.0]
     },
    {"category": "CA",
     "weight": 15,
     "grades": [100.0, 100.0, 98.0, 95.0, 0.0, 100.0]
     },
    {"category": "LA",
     "weight": 25.0,
     "grades": [100.0, 100.0, 100.0, 5.0, 0.0, 70.0]
     },
    {"category": "Quiz",
     "weight": 25,
     "grades": []
     },
    {"category": "Project",
     "weight": 25,
     "grades": []
     }
]

while True:
    print_main_menu(the_menu)  #
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper()  # to allow us to input lower- or upper-case letters

    if opt not in the_menu:
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected option {opt} to > {the_menu[opt]}.")

    if opt == "Q":  # TODO 4: quit the program
        print("Goodbye!\n")
        print("See you next time!")
        break  # exit the main `while` loop

    input("::: Press Enter to continue")

    if opt == "T":
        total = get_total_grade(all_grades, True)
        print(f"Current total is {total:.2f}")


    elif opt == "L":
        subopt = get_selection(the_menu[opt], submenu)
        if subopt == 'C':
            print_grade_info(all_grades, show_grades=False)

        elif subopt == 'G':
            print_grade_info(all_grades)
    elif opt == 'A':
        add_helper()

    elif opt == 'U':
        update_helper()

    elif opt == 'D':
        delete_helper()
