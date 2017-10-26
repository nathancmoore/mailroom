"""A command line application to streamline writing thank you notes.

Also contains commands to see a list of donors, quit, or
 start over the process.
"""

from terminaltables import AsciiTable
import os
import sys

donors = {}

last_input = ""


def quit_or_restart(user_entry):
    """Allow the user to restart the prompts or quit the app."""
    if user_entry == "quit":
        sys.exit()
    if user_entry == "restart":
        init_prompts()


def generate_donor_names():
    """Use Faker to create a list of fake donors."""
    from faker import Factory
    donor_names = []

    for i in range(20):
        raw_name = Factory.create().name().split()
        usable_name = raw_name[0] + " " + raw_name[1]
        donor_names.append(usable_name)

    return donor_names


def generate_donations(donor_name_list):
    """Randomly generate 1-10 random donations and store them as lists."""
    import random

    all_donations = []

    for name in donor_name_list:
        donations = []
        num_of_donations = random.randint(1, 10)
        for i in range(num_of_donations):
            donations.append(random.randint(20, 500))

        all_donations.append(donations)

    return all_donations


def build_dictionary():
    """Write keys and values to the dictionary."""
    names = generate_donor_names()
    donations = generate_donations(names)
    for i in range(20):
        donors[names[i]] = donations[i]


def init_thankyous():
    """Prompt the user for full name or to request a list."""
    last_input = input("To write a thank you, enter the donor's full name \
        (case sensitive).\nTo see a list of all donors, enter list. \
        \n\n >>>>Make your selection: ")
    quit_or_restart(last_input)
    if last_input.lower() == "list":
        for donor in donors:
            print(donor)
        init_thankyous()

    elif len(last_input.split()) != 2:
        print("Invalid Entry. Read the instructions carefully!")

        init_thankyous()

    elif last_input in donors.keys():
        ask_for_amount(last_input)
        os.system('clear')

    else:
        donors[last_input] = []
        ask_for_amount(last_input)
        os.system('clear')


def ask_for_amount(donor):
    """Function that asks the user for donation amount."""
    last_input = input("Please enter donation amount: $")
    quit_or_restart(last_input)

    try:
        float(last_input)
    except ValueError:
        print("Invalid Entry. Read the instructions carefully!")
        ask_for_amount(donor)

    if float(last_input) > 0:
        donors[donor].append(float(last_input))
        compose_thank_you_message(donor, last_input)
    else:
        print("Invalid Entry. Read the instructions carefully!")
        ask_for_amount(donor)


def compose_thank_you_message(donor, amount):
    """Create the thank you message."""
    print("Thank you {} for your donation of ${}".format(donor, amount))
    init_prompts()


def init_report():
    """Create a table showing donation histories."""
    table_data = [
        ['Name', 'Amount', 'Total', 'Average'],
    ]

    for idx, donor in enumerate(donors):
        sort = sorted(donors.items(), key=lambda x: sum(x[1]), reverse=True)
        table_data.append(
            [sort[idx][0], sort[idx][1], sum(sort[idx][1]),
             sum(sort[idx][1]) / len(sort[idx][1])])
    table = AsciiTable(table_data)
    print(table.table)
    init_prompts()


def init_prompts():
    """User chooses whether to write thank yous or see report."""
    last_input = input("To write thank yous, enter 1. \
        \nTo see a report, enter 2.\n\n At any time, enter quit to quit\n \
        or restart to restart\n\n\n>>>>Make your selection: ")
    quit_or_restart(last_input)

    if last_input == "1":
        os.system('clear')
        init_thankyous()

    elif last_input == "2":
        os.system('clear')
        init_report()

    else:
        print("Invalid Entry. Read the instructions carefully!")
        init_prompts()


if __name__ == "__main__":
    os.system('clear')
    build_dictionary()
    init_prompts()
