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
