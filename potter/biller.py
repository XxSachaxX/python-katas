from constants import BASE_AMOUNT_PER_BOOK, FIRST_BOOK, SECOND_BOOK

BASE_DISCOUNT_MULTIPLIER = 0.95

def bill(list_of_books):
    number_of_books = len(list_of_books)
    number_of_different_books = get_number_of_different_books(list_of_books)

    if number_of_different_books != 0:
        if number_of_books == 3:
            bill_for_different_books = (number_of_different_books * BASE_AMOUNT_PER_BOOK) * BASE_DISCOUNT_MULTIPLIER

            return bill_for_different_books + BASE_AMOUNT_PER_BOOK
        else:
            return (BASE_AMOUNT_PER_BOOK * number_of_books) * BASE_DISCOUNT_MULTIPLIER

    return BASE_AMOUNT_PER_BOOK * number_of_books

def get_number_of_different_books(list_of_books):
    nb_of_copies_of_first_book = list_of_books.count(FIRST_BOOK)
    nb_of_copies_of_second_book = list_of_books.count(SECOND_BOOK)

    if nb_of_copies_of_first_book > 0 and nb_of_copies_of_second_book > 0:
        return 2
    else:
        return 0
