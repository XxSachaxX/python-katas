from biller import bill
from biller import BASE_AMOUNT_PER_BOOK

def test_biller_exists():
    assert callable(bill)

def test_with_a_single_book_from_the_series():
    book = "Harry Potter and the Sorcerer's Stone"
    expected = BASE_AMOUNT_PER_BOOK

    assert bill([book]) == expected, f"The amount due for {book} should be {expected}"
