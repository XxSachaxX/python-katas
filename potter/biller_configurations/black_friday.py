class BlackFridayBillerConfiguration():

    def discounts(self):
        return {
            "standard_rate": {"nb_of_books_required": 1, "discount_multiplier": 1},
            "two_books_discount_multiplier": {"nb_of_books_required": 2, "discount_multiplier": 0.9},
            "three_books_discount_multiplier": {"nb_of_books_required": 3, "discount_multiplier": 0.8},
            "four_books_discount_multiplier": {"nb_of_books_required": 4, "discount_multiplier": 0.7},
            "five_books_discount_multiplier": {"nb_of_books_required": 5, "discount_multiplier": 0.5}
        }


    def base_amount_per_book(self):
        return 5
