from constants import BASE_AMOUNT_PER_BOOK

def bill(list_of_books):
    return BASE_AMOUNT_PER_BOOK * len(list_of_books)
