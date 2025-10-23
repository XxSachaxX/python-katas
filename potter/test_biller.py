from biller import Biller
from biller_configurations.default import DefaultBillerConfiguration
from biller_configurations.black_friday import BlackFridayBillerConfiguration
from books_series_configurations.harry_potter import HarryPotterSeries
from books_series_configurations.realm_of_the_elderlings import RealmOfTheElderlingSeries

# Tests with default configuration
default_biller_configuration = DefaultBillerConfiguration()
happy_potter_series_configuration = HarryPotterSeries()
first_book, second_book, third_book, fourth_book, fifth_book = happy_potter_series_configuration.books()

def test_with_a_single_book():
    biller = Biller([first_book], default_biller_configuration, happy_potter_series_configuration)
    result = biller.bill()
    expected = default_biller_configuration.base_amount_per_book()

    assert result == expected, f"The amount due should be {expected} but is {result}"


def test_with_two_identical_books():
    biller = Biller([first_book, first_book], default_biller_configuration, happy_potter_series_configuration)
    result = biller.bill()
    expected = 16

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_different_books():
    biller = Biller([first_book, second_book], default_biller_configuration, happy_potter_series_configuration)
    result = biller.bill()
    expected = 15.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_identical_books_and_a_different_one():
    biller = Biller([first_book,second_book,first_book], default_biller_configuration, happy_potter_series_configuration)
    result = biller.bill()
    expected = 23.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_identical_books_and_a_different_one_in_a_different_order():
    biller = Biller([first_book,first_book,second_book], default_biller_configuration, happy_potter_series_configuration)
    result = biller.bill()
    expected = 23.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_three_identical_books():
    biller = Biller([first_book,first_book,first_book], default_biller_configuration, happy_potter_series_configuration)
    result = biller.bill()
    expected = 24

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_three_different_books():
    biller = Biller([first_book,second_book,third_book], default_biller_configuration, happy_potter_series_configuration)
    result = biller.bill()
    expected = 21.6

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_four_different_books():
    biller = Biller([first_book,second_book,third_book, fourth_book], default_biller_configuration, happy_potter_series_configuration)
    result = biller.bill()
    expected = 25.6

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_four_identical_books():
    biller = Biller([first_book,first_book,first_book,first_book], default_biller_configuration, happy_potter_series_configuration)
    result = biller.bill()
    expected = 32

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_real_complete_basket():
    biller = Biller([first_book,first_book,second_book,second_book,third_book,third_book,fourth_book,fifth_book], default_biller_configuration, happy_potter_series_configuration)
    result = biller.bill()
    expected = 51.60

    assert result == expected, f"The amount due should be {expected} but is {result}"

# Test with different book series

realm_of_the_elderlings_series_configuration = RealmOfTheElderlingSeries()
tome_one, tome_two, tome_three, tome_four, tome_five, tome_six, tome_seven, tome_eight, tome_nine, tome_ten, tome_eleven, tome_twelve, tome_thirteen = realm_of_the_elderlings_series_configuration.books()
def test_with_a_single_book_from_other_series():
    biller = Biller([tome_one], default_biller_configuration, realm_of_the_elderlings_series_configuration)
    result = biller.bill()
    expected = default_biller_configuration.base_amount_per_book()

    assert result == expected, f"The amount due should be {expected} but is {result}"


def test_with_two_identical_books_from_other_series():
    biller = Biller([tome_one, tome_one], default_biller_configuration, realm_of_the_elderlings_series_configuration)
    result = biller.bill()
    expected = 16

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_different_books_from_other_series():
    biller = Biller([tome_one, tome_two], default_biller_configuration, realm_of_the_elderlings_series_configuration)
    result = biller.bill()
    expected = 15.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_identical_books_and_a_different_one_from_other_series():
    biller = Biller([tome_one,tome_two,tome_one], default_biller_configuration, realm_of_the_elderlings_series_configuration)
    result = biller.bill()
    expected = 23.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_two_identical_books_and_a_different_one_in_a_different_order_from_other_series():
    biller = Biller([tome_one,tome_one,tome_two], default_biller_configuration, realm_of_the_elderlings_series_configuration)
    result = biller.bill()
    expected = 23.2

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_three_identical_books_from_other_series():
    biller = Biller([tome_one,tome_one,tome_one], default_biller_configuration, realm_of_the_elderlings_series_configuration)
    result = biller.bill()
    expected = 24

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_three_different_books_from_other_series():
    biller = Biller([tome_one,tome_two,tome_three], default_biller_configuration, realm_of_the_elderlings_series_configuration)
    result = biller.bill()
    expected = 21.6

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_four_different_books_from_other_series():
    biller = Biller([tome_one,tome_two,tome_three, tome_four], default_biller_configuration, realm_of_the_elderlings_series_configuration)
    result = biller.bill()
    expected = 25.6

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_four_identical_books_from_other_series():
    biller = Biller([tome_one,tome_one,tome_one,tome_one], default_biller_configuration, realm_of_the_elderlings_series_configuration)
    result = biller.bill()
    expected = 32

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_basket_from_other_series():
    biller = Biller([tome_one,tome_one,tome_two,tome_two,tome_three,tome_three,tome_four,tome_five], default_biller_configuration, realm_of_the_elderlings_series_configuration)
    result = biller.bill()
    expected = 51.60

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_full_other_series():
    biller = Biller([tome_one,tome_two,tome_three,tome_four,tome_five,tome_six,tome_seven,tome_eight,tome_nine,tome_ten,tome_eleven,tome_twelve,tome_thirteen], default_biller_configuration, realm_of_the_elderlings_series_configuration)
    result = biller.bill()
    expected = 78

    assert result == expected, f"The amount due should be {expected} but is {result}"

def test_with_double_full_other_series():
    biller = Biller([
        tome_one,tome_two,tome_three,tome_four,tome_five,tome_six,tome_seven,tome_eight,tome_nine,tome_ten,tome_eleven,tome_twelve,tome_thirteen,
        tome_one,tome_two,tome_three,tome_four,tome_five,tome_six,tome_seven,tome_eight,tome_nine,tome_ten,tome_eleven,tome_twelve,tome_thirteen
    ],
    default_biller_configuration, realm_of_the_elderlings_series_configuration)
    result = biller.bill()
    expected = 156

    assert result == expected, f"The amount due should be {expected} but is {result}"

# Test with other biller configuration

black_friday_biller_configuration = BlackFridayBillerConfiguration()

def test_with_real_complete_basket_on_black_friday():
    biller = Biller([first_book,first_book,second_book,second_book,third_book,third_book,fourth_book,fifth_book], black_friday_biller_configuration, happy_potter_series_configuration)
    result = biller.bill()
    expected = 24.50

    assert result == expected, f"The amount due should be {expected} but is {result}"
