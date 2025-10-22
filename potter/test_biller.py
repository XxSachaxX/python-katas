from biller import bill, get_books_counts, get_books_counts_by_discount_multiplier
from constants import (
    BASE_AMOUNT_PER_BOOK, FIRST_BOOK,
    SECOND_BOOK, THIRD_BOOK,
    FOURTH_BOOK, FIFTH_BOOK,
    TWO_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER,
    THREE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER,
    FOUR_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER,
    STANDARD_RATE, FIVE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER)

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

def test_with_three_different_books():
    result = bill([FIRST_BOOK,SECOND_BOOK,THIRD_BOOK])
    expected = 21.6

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_four_different_books():
    result = bill([FIRST_BOOK,SECOND_BOOK,THIRD_BOOK, FOURTH_BOOK])
    expected = 25.6

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_four_identical_books():
    result = bill([FIRST_BOOK,FIRST_BOOK,FIRST_BOOK,FIRST_BOOK])
    expected = 32

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_ultimate():
    result = bill([FIRST_BOOK,FIRST_BOOK,SECOND_BOOK,SECOND_BOOK,THIRD_BOOK,THIRD_BOOK,FOURTH_BOOK,FIFTH_BOOK])
    expected = 51.60

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_get_books_counts():
    result = get_books_counts([FIRST_BOOK, FIRST_BOOK, SECOND_BOOK, THIRD_BOOK, FOURTH_BOOK, FOURTH_BOOK])
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

    expected = {
    STANDARD_RATE: 5,
    TWO_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER: 0,
    THREE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER: 0,
    FOUR_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER: 0,
    FIVE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER: 0
    }

    result = get_books_counts_by_discount_multiplier(list_of_books)

    assert result == expected, f"Expected: {expected} but got: {result}"

def test_books_counts_by_discount_multiplier_with_one_copy_of_two_books():
    list_of_books = [FIRST_BOOK,FIFTH_BOOK]

    expected = {
    STANDARD_RATE: 0,
    TWO_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER: 2,
    THREE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER: 0,
    FOUR_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER: 0,
    FIVE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER: 0
    }

    result = get_books_counts_by_discount_multiplier(list_of_books)

    assert result == expected, f"Expected: {expected} but got: {result}"
