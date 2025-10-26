def get_bundles(inventory):
    unique_books = []
    duplicates = []
    bundles = []

    for book in inventory:
        if book not in unique_books:
            unique_books.append(book)
        else:
            duplicates.append(book)

    bundles.append(unique_books)

    for duplicate in duplicates:
        bundles.append([duplicate])

    return bundles
