"""A command line application to streamline writing thank you notes.

Also contains commands to see a list of donors, quit, or
 start over the process.
"""

donors = {}


def generate_donor_names():
    """Use Faker to create a list of fake donors."""
    from faker import Factory
    donor_names = []

    for i in range(100):
        donor_names.append(Factory.create().name())

    return donor_names


def generates_donations(donor_name_list):
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
