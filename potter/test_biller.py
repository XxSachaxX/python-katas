from biller import bill
from constants import BASE_AMOUNT_PER_BOOK, FIRST_BOOK, SECOND_BOOK

def test_biller_exists():
    assert callable(bill)

def test_with_a_single_book():
    result = bill([FIRST_BOOK])
    expected = BASE_AMOUNT_PER_BOOK

    assert result == expected, f"The amount due should be {expected} but is {result}"


def test_with_two_identical_books():
    result = bill([FIRST_BOOK, FIRST_BOOK])
    expected = 16

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_different_books():
    result = bill([FIRST_BOOK, SECOND_BOOK])
    expected = 15.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_identical_books_and_a_different_one():
    result = bill([FIRST_BOOK,SECOND_BOOK,FIRST_BOOK])
    expected = 23.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_identical_books_and_a_different_one_in_a_different_order():
    result = bill([FIRST_BOOK,FIRST_BOOK,SECOND_BOOK])
    expected = 23.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_three_identical_books():
    result = bill([FIRST_BOOK,FIRST_BOOK,FIRST_BOOK])
    expected = 24

    assert result == expected, f"The amount due should be {expected} but is {result}"
