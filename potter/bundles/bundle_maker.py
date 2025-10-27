class BundleMaker():
    def __init__(self, inventory):
        self.inventory = inventory

    def get_bundles(self):
        bundles = []
        books_counts = {}

        for book in self.inventory:
            if book not in books_counts.keys():
                books_counts[book] = 1
            else:
                books_counts[book] += 1

        max_number_of_books = max(list(books_counts.values()))

        for i in range(max_number_of_books):
            bundle = []

            for book, count in books_counts.items():
                if count > 0 and book not in bundle:
                    bundle.append(book)
                    books_counts[book] -= 1

            bundles.append(bundle)

        return bundles
