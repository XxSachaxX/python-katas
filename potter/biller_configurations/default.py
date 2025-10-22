from constants import BASE_AMOUNT_PER_BOOK, FIVE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER, FOUR_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER, STANDARD_RATE, THREE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER, TWO_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER


class DefaultBillerConfiguration():

    def base_amount_per_book(self):
        return BASE_AMOUNT_PER_BOOK

    def standard_rate(self):
        return STANDARD_RATE

    def two_books_discount_multiplier(self):
        return TWO_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER

    def three_books_discount_multiplier(self):
        return THREE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER

    def four_books_discount_multiplier(self):
        return FOUR_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER

    def five_books_discount_multiplier(self):
        return FIVE_DIFFERENT_BOOKS_DISCOUNT_MULTIPLIER
