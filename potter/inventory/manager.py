class Manager():

    def __init__(self, inventory):
        self.inventory = inventory

    def remove_books(self, books_to_remove):
        for series_name, books in books_to_remove.items():
            for book, count in books.items():
                if series_name not in self.inventory:
                    continue

                self.inventory[series_name][book] -= count

        return
