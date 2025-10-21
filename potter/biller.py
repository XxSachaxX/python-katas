from constants import BASE_AMOUNT_PER_BOOK

BASE_DISCOUNT_MULTIPLIER = 0.95

def bill(list_of_books):
    number_of_books = len(list_of_books)

    if number_of_books > 1 and list_of_books[0] != list_of_books[1]:
        return (BASE_AMOUNT_PER_BOOK * number_of_books) * BASE_DISCOUNT_MULTIPLIER

    return BASE_AMOUNT_PER_BOOK * number_of_books
