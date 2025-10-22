from constants import (
    FIRST_BOOK, FOURTH_BOOK,
    SECOND_BOOK, THIRD_BOOK,
    FIFTH_BOOK
)

class Biller():
    def __init__(self, list_of_books, biller_configuration):
        self.list_of_books = list_of_books
        self.biller_configuration = biller_configuration

    def bill(self):
        books_counts_by_discount_multiplier = self.get_books_counts_by_discount_multiplier()

        total = 0
        for key, value in books_counts_by_discount_multiplier.items():
            total += (self.biller_configuration.base_amount_per_book(self) * value) * key

        return total

    def get_books_counts(self):
        return {
            FIRST_BOOK: self.list_of_books.count(FIRST_BOOK),
            SECOND_BOOK: self.list_of_books.count(SECOND_BOOK),
            THIRD_BOOK: self.list_of_books.count(THIRD_BOOK),
            FOURTH_BOOK: self.list_of_books.count(FOURTH_BOOK),
            FIFTH_BOOK: self.list_of_books.count(FIFTH_BOOK)
        }

    def get_books_counts_by_discount_multiplier(self):
        books_counts = self.get_books_counts()

        rates = {
        self.biller_configuration.standard_rate(self): 0,
        self.biller_configuration.two_books_discount_multiplier(self): 0,
        self.biller_configuration.three_books_discount_multiplier(self): 0,
        self.biller_configuration.four_books_discount_multiplier(self): 0,
        self.biller_configuration.five_books_discount_multiplier(self): 0
        }

        max_number_of_books = max(list(books_counts.values()))

        for i in range(max_number_of_books):
            number_of_books_for_round = 0

            for key, value in books_counts.items():
                if value > 0:
                    books_counts[key] -= 1
                    number_of_books_for_round += 1

            if number_of_books_for_round == 5:
                rates[self.biller_configuration.five_books_discount_multiplier(self)] += 5
            elif number_of_books_for_round == 4:
                rates[self.biller_configuration.four_books_discount_multiplier(self)] += 4
            elif number_of_books_for_round == 3:
                rates[self.biller_configuration.three_books_discount_multiplier(self)] += 3
            elif number_of_books_for_round == 2:
                rates[self.biller_configuration.two_books_discount_multiplier(self)] += 2
            elif number_of_books_for_round == 1:
                rates[self.biller_configuration.standard_rate(self)] += 1

        return rates
