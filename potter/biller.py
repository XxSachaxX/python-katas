from constants import (
    FIRST_BOOK, FOURTH_BOOK,
    SECOND_BOOK, THIRD_BOOK,
    FIFTH_BOOK
)

class Biller():
    def __init__(self, list_of_books, biller_configuration):
        self.list_of_books = list_of_books
        self.base_amount_per_book = biller_configuration.base_amount_per_book()
        self.standard_rate = biller_configuration.standard_rate()
        self.two_books_discount_multiplier = biller_configuration.two_books_discount_multiplier()
        self.three_books_discount_multiplier = biller_configuration.three_books_discount_multiplier()
        self.four_books_discount_multiplier = biller_configuration.four_books_discount_multiplier()
        self.five_books_discount_multiplier = biller_configuration.five_books_discount_multiplier()

    def bill(self):
        books_counts_by_discount_multiplier = self.__get_books_counts_by_discount_multiplier()

        total = 0
        for rate, nb_of_books in books_counts_by_discount_multiplier.items():
            total += (self.base_amount_per_book * nb_of_books) * rate

        return total

    def __get_books_counts(self):
        books_counts = {}

        for book in self.__all_books():
            books_counts[book] = self.list_of_books.count(book)

        return books_counts

    def __all_books(self):
        return [FIRST_BOOK,SECOND_BOOK,THIRD_BOOK,FOURTH_BOOK,FIFTH_BOOK]

    def __get_books_counts_by_discount_multiplier(self):
        books_counts = self.__get_books_counts()

        rates = {
        self.standard_rate: 0,
        self.two_books_discount_multiplier: 0,
        self.three_books_discount_multiplier: 0,
        self.four_books_discount_multiplier: 0,
        self.five_books_discount_multiplier: 0
        }

        max_number_of_books = max(list(books_counts.values()))

        for i in range(max_number_of_books):
            number_of_books_for_round = 0

            for key, value in books_counts.items():
                if value > 0:
                    books_counts[key] -= 1
                    number_of_books_for_round += 1


            rates_per_nb_of_books = self.__get_rates_per_number_of_books()

            rate = rates_per_nb_of_books[number_of_books_for_round]
            rates[rate] += number_of_books_for_round

        return rates

    def __get_rates_per_number_of_books(self):
        return {
            5: self.five_books_discount_multiplier,
            4: self.four_books_discount_multiplier,
            3: self.three_books_discount_multiplier,
            2: self.two_books_discount_multiplier,
            1: self.standard_rate
        }
