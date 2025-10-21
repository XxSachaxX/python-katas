from constants import BASE_AMOUNT_PER_BOOK

def bill(list_of_books):
    if len(list_of_books) > 1 and list_of_books[0] != list_of_books[1]:
        return (BASE_AMOUNT_PER_BOOK * len(list_of_books)) * 0.95

    return BASE_AMOUNT_PER_BOOK * len(list_of_books)
