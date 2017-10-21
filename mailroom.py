"""A command line application to streamline writing thank you notes.

Also contains commands to see a list of donors, quit, or
 start over the process.
"""
from builtins import input

donors = {}

last_input = ""


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
    """Write something here."""
    last_input = input("To write a thank you, enter the donor's full name (case sensitive).\nTo see a list of all donors, enter list. \n\n >>>>Make your selection: ")

    if last_input.lower() == "list":
        for donor in donors:
            print(donor)

        print("\n\n\n")

        init_thankyous()

    elif len(last_input.split()) != 2:
        print("Invalid Entry. Read the instructions carefully!")

        init_thankyous()

    elif last_input in donors.keys():
        ask_for_amount(last_input)

    else:
        donors[last_input] = []
        ask_for_amount(last_input)


def ask_for_amount(donor):
    """Function that asks the user for donation amount."""
    last_input = input("Please enter donation amount: $")

    if last_input.isnumeric():
        donors[donor].append(int(last_input))
        compose_thank_you_message(donor, last_input)
    else:
        print("Invalid Entry. Read the instructions carefully!")
        ask_for_amount()


def compose_thank_you_message(donor, amount):
    """Function to create the thank you message."""
    donor_name = donors[donor]
    print("Thank you {} for your donation of ${}".format(donor, amount))
    init_prompts()


def init_report():
    """Write something here."""
    for idx, donor in enumerate(donors):
        donation_list = donors[donor]
        total_donations = sum(donors[donor])
        average_donation = total_donations / len(donors[donor])
        sort = sorted(donors.items(), key=lambda x: sum(x[1]), reverse=True)
        print("Name: {} \n List of Donations: {} \n Total: {} \n Average: {}".format(sort[idx][0], sort[idx][1], sum(sort[idx][1]), sum(sort[idx][1]) / len(sort[idx][1])))
        # print("{}:\nTotal donations: {}\nList of donations: {}\nAverage donation: {}\n".format(donor, total_donations, donation_list, average_donation))

    init_prompts()


def init_prompts():
    """User chooses whether to write thank yous or see report."""
    last_input = input("\n\n\n\nTo write thank yous, enter 1. \nTo see a report, enter 2.\n\n >>>>Make your selection: ")

    if int(last_input) == 1:
        init_thankyous()

    elif int(last_input) == 2:
        init_report()

    else:
        print("Invalid Entry. Read the instructions carefully!")
        init_prompts()


if __name__ == "__main__":
    build_dictionary()
    init_prompts()
