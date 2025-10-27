class BundleMaker():
    def __init__(self, inventory, chosen_series):
        self.inventory = inventory
        self.chosen_series = chosen_series

    def get_bundles_for_chosen_series(self):
        bundles = []
        books_counts = self.inventory[self.chosen_series]
        max_number_of_books = max(list(books_counts.values()))

        for i in range(max_number_of_books):
            bundle = []

            for book, count in books_counts.items():
                if count > 0 and book not in bundle:
                    bundle.append(book)
                    books_counts[book] -= 1

            bundles.append(bundle)

        return bundles
