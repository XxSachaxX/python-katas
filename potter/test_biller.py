from biller import Biller
from constants import (
    BASE_AMOUNT_PER_BOOK, FIRST_BOOK,
    SECOND_BOOK, THIRD_BOOK,
    FOURTH_BOOK, FIFTH_BOOK)
from biller_configurations.default import DefaultBillerConfiguration

biller_configuration = DefaultBillerConfiguration()

def test_with_a_single_book():
    biller = Biller([FIRST_BOOK], biller_configuration)
    result = biller.bill()
    expected = BASE_AMOUNT_PER_BOOK

    assert result == expected, f"The amount due should be {expected} but is {result}"


def test_with_two_identical_books():
    biller = Biller([FIRST_BOOK, FIRST_BOOK], biller_configuration)
    result = biller.bill()
    expected = 16

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_different_books():
    biller = Biller([FIRST_BOOK, SECOND_BOOK], biller_configuration)
    result = biller.bill()
    expected = 15.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_identical_books_and_a_different_one():
    biller = Biller([FIRST_BOOK,SECOND_BOOK,FIRST_BOOK], biller_configuration)
    result = biller.bill()
    expected = 23.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_identical_books_and_a_different_one_in_a_different_order():
    biller = Biller([FIRST_BOOK,FIRST_BOOK,SECOND_BOOK], biller_configuration)
    result = biller.bill()
    expected = 23.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_three_identical_books():
    biller = Biller([FIRST_BOOK,FIRST_BOOK,FIRST_BOOK], biller_configuration)
    result = biller.bill()
    expected = 24

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_three_different_books():
    biller = Biller([FIRST_BOOK,SECOND_BOOK,THIRD_BOOK], biller_configuration)
    result = biller.bill()
    expected = 21.6

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_four_different_books():
    biller = Biller([FIRST_BOOK,SECOND_BOOK,THIRD_BOOK, FOURTH_BOOK], biller_configuration)
    result = biller.bill()
    expected = 25.6

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_four_identical_books():
    biller = Biller([FIRST_BOOK,FIRST_BOOK,FIRST_BOOK,FIRST_BOOK], biller_configuration)
    result = biller.bill()
    expected = 32

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_real_complete_basket():
    biller = Biller([FIRST_BOOK,FIRST_BOOK,SECOND_BOOK,SECOND_BOOK,THIRD_BOOK,THIRD_BOOK,FOURTH_BOOK,FIFTH_BOOK], biller_configuration)
    result = biller.bill()
    expected = 51.60

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_get_books_counts():
    biller = Biller([FIRST_BOOK, FIRST_BOOK, SECOND_BOOK, THIRD_BOOK, FOURTH_BOOK, FOURTH_BOOK], biller_configuration)
    result = biller._get_books_counts()
    expected = {
        FIRST_BOOK: 2,
        SECOND_BOOK: 1,
        THIRD_BOOK: 1,
        FOURTH_BOOK: 2,
        FIFTH_BOOK: 0
    }

    assert result == expected, f"Expected: {expected} but got: {result}"

def test_books_counts_by_discount_multiplier_with_five_copies_of_one_book():
    list_of_books = [FIRST_BOOK,FIRST_BOOK,FIRST_BOOK,FIRST_BOOK, FIRST_BOOK]
    biller = Biller(list_of_books, biller_configuration)

    expected = {
    biller_configuration.standard_rate(): 5,
    biller_configuration.two_books_discount_multiplier(): 0,
    biller_configuration.three_books_discount_multiplier(): 0,
    biller_configuration.four_books_discount_multiplier(): 0,
    biller_configuration.five_books_discount_multiplier(): 0
    }

    result = biller._get_books_counts_by_discount_multiplier()

    assert result == expected, f"Expected: {expected} but got: {result}"

def test_books_counts_by_discount_multiplier_with_one_copy_of_two_books():
    list_of_books = [FIRST_BOOK,FIFTH_BOOK]
    biller = Biller(list_of_books, biller_configuration)

    expected = {
    biller_configuration.standard_rate(): 0,
    biller_configuration.two_books_discount_multiplier(): 2,
    biller_configuration.three_books_discount_multiplier(): 0,
    biller_configuration.four_books_discount_multiplier(): 0,
    biller_configuration.five_books_discount_multiplier(): 0
    }

    result = biller._get_books_counts_by_discount_multiplier()

    assert result == expected, f"Expected: {expected} but got: {result}"
