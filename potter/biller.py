from constants import (
    BASE_AMOUNT_PER_BOOK,
    FIRST_BOOK, FOURTH_BOOK,
    SECOND_BOOK, THIRD_BOOK,
    FIFTH_BOOK, TWO_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER,
    FOUR_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER, THREE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER,
    STANDARD_RATE, FIVE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER)

class Biller():
    def __init__(self, list_of_books):
        self.list_of_books = list_of_books

    def bill(self):
        books_counts_by_discount_multiplier = self.get_books_counts_by_discount_multiplier()

        total = 0
        for key, value in books_counts_by_discount_multiplier.items():
            total += (BASE_AMOUNT_PER_BOOK * value) * key

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
        STANDARD_RATE: 0,
        TWO_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER: 0,
        THREE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER: 0,
        FOUR_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER: 0,
        FIVE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER: 0
        }

        max_number_of_books = max(list(books_counts.values()))

        for i in range(max_number_of_books):
            number_of_books_for_round = 0

            for key, value in books_counts.items():
                if value > 0:
                    books_counts[key] -= 1
                    number_of_books_for_round += 1

            if number_of_books_for_round == 5:
                rates[FIVE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER] += 5
            elif number_of_books_for_round == 4:
                rates[FOUR_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER] += 4
            elif number_of_books_for_round == 3:
                rates[THREE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER] += 3
            elif number_of_books_for_round == 2:
                rates[TWO_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER] += 2
            elif number_of_books_for_round == 1:
                rates[STANDARD_RATE] += 1

        return rates
