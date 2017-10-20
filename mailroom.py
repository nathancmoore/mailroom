"""A command line application to streamline writing thank you notes.

Also contains commands to see a list of donors, quit, or
 start over the process.
"""

donors = {}

last_input = ""


def generate_donor_names():
    """Use Faker to create a list of fake donors."""
    from faker import Factory
    donor_names = []

    for i in range(100):
        donor_names.append(Factory.create().name())

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
    for i in range(100):
        donors[names[i]] = donations[i]


def init_prompts():
    """User chooses whether to write thank yous or see report."""
    last_input = str(input("To write thank yous, enter 1. \nTo see a report, enter 2.\n\n Make your selection:  "))

    print(last_input)

    if last_input == 1:
        init_thankyous()
    elif last_input == 2:
        init_report()
    else:
        print("Invalid Entry. Read the instructions carefully!")
        init_prompts()


if __name__ == "__main__":
    build_dictionary()
    init_prompts()
