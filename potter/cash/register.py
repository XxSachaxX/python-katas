from potter.inventory.manager import Manager
from potter.billing.biller import Biller
# imports required for __get_books_series_configuration to work
from potter.books_series_configurations.harry_potter import HarryPotterSeries # noqa: F401
from potter.books_series_configurations.realm_of_the_elderlings import RealmOfTheElderlingsSeries # noqa: F401

class Register():

    def __init__(self, initial_cash_float, inventory, biller_configuration):
        self.cash_float = initial_cash_float
        self.inventory = inventory
        self.biller_configuration = biller_configuration

    def cash_in(self, customer_cart):
        self.__remove_books(customer_cart)

        total = 0
        for series_name, books_with_count in customer_cart.items():
            books_to_bill = []

            for book, count in books_with_count.items():
                for i in range(count):
                    books_to_bill.append(book)

            total += self.__bill(series_name, books_to_bill)

        self.cash_float -= total

    def __get_books_series_configuration(self, series_name):
        config_name = series_name.title().replace(" ", "") + "Series"
        cls = globals()[config_name]

        return cls()

    def __remove_books(self, customer_cart):
        Manager(self.inventory).remove_books(customer_cart)

    def __bill(self, series_name, books_to_bill):
        return Biller(books_to_bill, self.biller_configuration, self.__get_books_series_configuration(series_name)).bill()
