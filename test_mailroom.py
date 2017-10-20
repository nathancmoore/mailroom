"""Various test for our mailroom.py file."""


import pytest


def test_generated_donor_names():
    """Test that random names are generated."""
    from mailroom import generate_donor_names
    donor_names = generate_donor_names()
    assert donor_names


def test_names_are_strings():
    """Test that the names are all strings."""
    from mailroom import generate_donor_names
    donor_names = generate_donor_names()
    for name in donor_names:
        assert type(name) == str


def test_random_donation_amounts():
    """Test that random amounts are created for donations."""
    from mailroom import generate_donations
    donations = generate_donations(['bill', 'bob', 'joe'])
    assert len(donations) != 0


def test_multiple_donation_amounts():
    """Test that each donor has multiple donation amounts."""
    from mailroom import generate_donations
    donations = generate_donations(['bill', 'bob', 'joe'])
    for i in range(len(donations)):
        assert donations[i] != 0


def test_dictionary():
    """Test that that dictionary is not empty."""
    import mailroom
    mailroom.build_dictionary()
    assert mailroom.donors.keys() != 0


def test_dictionary_values():
    """Test there are values attached to keys in the dictionary."""
    import mailroom
    mailroom.build_dictionary()
    for key in mailroom.donors:
        value = mailroom.donors.get(key)
        assert value != 0
