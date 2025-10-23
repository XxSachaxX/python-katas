class Biller():
    def __init__(self, list_of_books, biller_configuration, books_series_configuration):
        self.list_of_books = list_of_books
        self.__books_series = books_series_configuration.books()
        self.__base_amount_per_book = biller_configuration.base_amount_per_book()
        self.__standard_rate = biller_configuration.standard_rate()
        self.__small_discount_multiplier = biller_configuration.two_books_discount_multiplier()
        self.__medium_discount_multiplier = biller_configuration.three_books_discount_multiplier()
        self.__large_discount_multiplier = biller_configuration.four_books_discount_multiplier()
        self.__complete_series_discount_multiplier = biller_configuration.five_books_discount_multiplier()


    def bill(self):
        books_counts_by_discount_multiplier = self.__get_books_counts_by_discount_multiplier()

        total = 0
        for rate, nb_of_books in books_counts_by_discount_multiplier.items():
            total += (self.__base_amount_per_book * nb_of_books) * rate

        return total

    def __get_books_counts(self):
        books_counts = {}

        for book in self.__all_books():
            books_counts[book] = self.list_of_books.count(book)

        return books_counts

    def __all_books(self):
        return self.__books_series

    def __get_books_counts_by_discount_multiplier(self):
        books_counts = self.__get_books_counts()

        rates = {
        self.__standard_rate: 0,
        self.__small_discount_multiplier: 0,
        self.__medium_discount_multiplier: 0,
        self.__large_discount_multiplier: 0,
        self.__complete_series_discount_multiplier: 0
        }

        max_number_of_books = max(list(books_counts.values()))

        for i in range(max_number_of_books):
            number_of_books_for_round = 0

            for book, count in books_counts.items():
                if count > 0:
                    books_counts[book] -= 1
                    number_of_books_for_round += 1


            rates_per_nb_of_books = self.__get_rates_per_number_of_books()
            rate = rates_per_nb_of_books[number_of_books_for_round]
            rates[rate] += number_of_books_for_round

        return rates

    def __get_rates_per_number_of_books(self):
        return {
            5: self.__complete_series_discount_multiplier,
            4: self.__large_discount_multiplier,
            3: self.__medium_discount_multiplier,
            2: self.__small_discount_multiplier,
            1: self.__standard_rate
        }
