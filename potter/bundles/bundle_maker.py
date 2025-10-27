class BundleMaker():
    def __init__(self, inventory):
        self.inventory = inventory

    def get_bundles(self):
        series_names = self.inventory.keys()
        bundles = []

        for name in series_names:
            bundles_for_series = self.__get_bundles_for_series(name)

            for bundle in bundles_for_series:
                bundles.append({"series_name": name, "content": bundle})

        return bundles

    def __get_bundles_for_series(self, series_name):
        bundles = []
        books_counts = self.inventory[series_name]
        max_number_of_books = max(list(books_counts.values()))

        for i in range(max_number_of_books):
            bundle = []

            for book, count in books_counts.items():
                if count > 0 and book not in bundle:
                    bundle.append(book)
                    books_counts[book] -= 1

            bundles.append(bundle)

        return bundles
