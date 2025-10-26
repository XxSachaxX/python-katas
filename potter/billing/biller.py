class Biller():
    def __init__(self, customer_cart, biller_configuration, books_series_configuration):
        self.customer_cart = customer_cart
        self.books_series = books_series_configuration.books()
        self.discounts = biller_configuration.discounts()
        self.__base_amount_per_book = biller_configuration.base_amount_per_book()

    def bill(self):
        books_counts_by_discount_multiplier = self.__get_books_counts_by_discount_multiplier()

        total = 0
        for rate, nb_of_books in books_counts_by_discount_multiplier.items():
            total += (self.__base_amount_per_book * nb_of_books) * rate

        return total

    def __get_books_counts(self):
        books_counts = {}

        for book in self.books_series:
            books_counts[book] = self.customer_cart.count(book)

        return books_counts

    def __get_books_counts_by_discount_multiplier(self):
        rates = {}
        for _, settings in self.discounts.items():
            rate = settings["discount_multiplier"]
            rates[rate] = 0

        books_counts = self.__get_books_counts()
        max_number_of_books = max(list(books_counts.values()))

        for i in range(max_number_of_books):
            number_of_books_for_round = 0

            for book, count in books_counts.items():
                if count > 0:
                    books_counts[book] -= 1
                    number_of_books_for_round += 1


            rates_per_nb_of_books = self.__get_rates_per_number_of_books()
            max_number_of_books_required = self.__get_max_required_nb_of_books()

            if number_of_books_for_round >= max_number_of_books_required:
                rate = rates_per_nb_of_books[max_number_of_books_required]
            else:
                rate = rates_per_nb_of_books[number_of_books_for_round]

            rates[rate] += number_of_books_for_round

        return rates

    def __get_max_required_nb_of_books(self):
        max = 0
        for rate_name, settings in self.discounts.items():
            if settings["nb_of_books_required"] > max:
                max = settings["nb_of_books_required"]

        return max

    def __get_rates_per_number_of_books(self):
        rates_per_number_of_books = {}

        for rate_name, settings in self.discounts.items():
            nb_of_books_required = settings["nb_of_books_required"]
            rate = settings["discount_multiplier"]
            rates_per_number_of_books[nb_of_books_required] = rate

        return rates_per_number_of_books
