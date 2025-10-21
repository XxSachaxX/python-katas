from biller import bill
from constants import BASE_AMOUNT_PER_BOOK, FIRST_BOOK, SECOND_BOOK

def test_biller_exists():
    assert callable(bill)

def test_with_a_single_book_from_the_series():
    expected = BASE_AMOUNT_PER_BOOK

    assert bill([FIRST_BOOK]) == expected, f"The amount due for {FIRST_BOOK} should be {expected}"

def test_with_two_identical_books_from_the_series():
    expected = 16

    assert bill([FIRST_BOOK, FIRST_BOOK])  == expected, f"The amount due for two copies of {FIRST_BOOK} should be {expected}"

def test_with_two_different_books_from_the_series():
    expected = 15.2

    assert bill([FIRST_BOOK, SECOND_BOOK])  == expected, f"The amount due for two copies of {FIRST_BOOK} should be {expected}"
