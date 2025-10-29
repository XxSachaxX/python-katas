class Manager():
    def __init__(self, inventory):
        self.inventory = inventory

    def remove_books(self, books_to_remove):
        for series_name, books in books_to_remove.items():
            for book, count in books.items():
                if series_name not in self.inventory:
                    continue

                if self.inventory[series_name][book] - count < 0:
                    self.inventory[series_name][book] = 0
                    continue

                self.inventory[series_name][book] -= count

        return

    def add_books(self, books_to_add):
        for series_name, books in books_to_add.items():
            for book, count in books.items():
                if series_name not in self.inventory:
                    self.inventory[series_name] = books
                    continue

                if self.inventory[series_name][book] > 0:
                    self.inventory[series_name][book] += count
                    continue

        return
