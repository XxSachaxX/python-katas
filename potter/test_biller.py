from biller import Biller
from constants import (
    FIRST_BOOK,
    SECOND_BOOK, THIRD_BOOK,
    FOURTH_BOOK, FIFTH_BOOK)
from biller_configurations.default import DefaultBillerConfiguration
from biller_configurations.black_friday import BlackFridayBillerConfiguration

default_biller_configuration = DefaultBillerConfiguration()

def test_with_a_single_book():
    biller = Biller([FIRST_BOOK], default_biller_configuration)
    result = biller.bill()
    expected = default_biller_configuration.base_amount_per_book()

    assert result == expected, f"The amount due should be {expected} but is {result}"


def test_with_two_identical_books():
    biller = Biller([FIRST_BOOK, FIRST_BOOK], default_biller_configuration)
    result = biller.bill()
    expected = 16

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_different_books():
    biller = Biller([FIRST_BOOK, SECOND_BOOK], default_biller_configuration)
    result = biller.bill()
    expected = 15.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_identical_books_and_a_different_one():
    biller = Biller([FIRST_BOOK,SECOND_BOOK,FIRST_BOOK], default_biller_configuration)
    result = biller.bill()
    expected = 23.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_identical_books_and_a_different_one_in_a_different_order():
    biller = Biller([FIRST_BOOK,FIRST_BOOK,SECOND_BOOK], default_biller_configuration)
    result = biller.bill()
    expected = 23.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_three_identical_books():
    biller = Biller([FIRST_BOOK,FIRST_BOOK,FIRST_BOOK], default_biller_configuration)
    result = biller.bill()
    expected = 24

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_three_different_books():
    biller = Biller([FIRST_BOOK,SECOND_BOOK,THIRD_BOOK], default_biller_configuration)
    result = biller.bill()
    expected = 21.6

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_four_different_books():
    biller = Biller([FIRST_BOOK,SECOND_BOOK,THIRD_BOOK, FOURTH_BOOK], default_biller_configuration)
    result = biller.bill()
    expected = 25.6

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_four_identical_books():
    biller = Biller([FIRST_BOOK,FIRST_BOOK,FIRST_BOOK,FIRST_BOOK], default_biller_configuration)
    result = biller.bill()
    expected = 32

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_real_complete_basket():
    biller = Biller([FIRST_BOOK,FIRST_BOOK,SECOND_BOOK,SECOND_BOOK,THIRD_BOOK,THIRD_BOOK,FOURTH_BOOK,FIFTH_BOOK], default_biller_configuration)
    result = biller.bill()
    expected = 51.60

    assert result == expected, f"The amount due should be {expected} but is {result}"


# Test with other biller configuration

black_friday_biller_configuration = BlackFridayBillerConfiguration()

def test_with_real_complete_basket_on_black_friday():
    biller = Biller([FIRST_BOOK,FIRST_BOOK,SECOND_BOOK,SECOND_BOOK,THIRD_BOOK,THIRD_BOOK,FOURTH_BOOK,FIFTH_BOOK], black_friday_biller_configuration)
    result = biller.bill()
    expected = 24.50

    assert result == expected, f"The amount due should be {expected} but is {result}"
