from potter.billing.biller import Biller
from potter.biller_configurations.black_friday import BlackFridayBillerConfiguration
from potter.books_series_configurations.harry_potter import HarryPotterSeries

black_friday_biller_configuration = BlackFridayBillerConfiguration()
happy_potter_series_configuration = HarryPotterSeries()
first_book, second_book, third_book, fourth_book, fifth_book = happy_potter_series_configuration.books()

def test_with_real_complete_basket_on_black_friday():
    biller = Biller([first_book,first_book,second_book,second_book,third_book,third_book,fourth_book,fifth_book], black_friday_biller_configuration, happy_potter_series_configuration)
    result = biller.bill()
    expected = 24.50

    assert result == expected, f"The amount due should be {expected} but is {result}"
