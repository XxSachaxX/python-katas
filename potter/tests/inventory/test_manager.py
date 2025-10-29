from potter.inventory.manager import Manager

def test_inventory_manager_does_nothing_when_passed_a_series_not_in_inventory():
    books_to_remove = {
        "A series that does not exist": {
            "A book that does not exist": 1
        }
    }

    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
            "Harry Potter and the Chamber of Secrets": 1,
            "Harry Potter and the Prisonner of Azkaban": 1,
            "Harry Potter and the Goblet of fire": 1,
            "Harry Potter and the Order of the Phoenix": 1,
            "Harry Potter and the Half-blood Prince": 1,
            "Harry Potter and the Deathly Hallows": 1
        }
    }

    expected = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
            "Harry Potter and the Chamber of Secrets": 1,
            "Harry Potter and the Prisonner of Azkaban": 1,
            "Harry Potter and the Goblet of fire": 1,
            "Harry Potter and the Order of the Phoenix": 1,
            "Harry Potter and the Half-blood Prince": 1,
            "Harry Potter and the Deathly Hallows": 1
        }
    }

    manager = Manager(inventory)
    manager.remove_books(books_to_remove)

    assert inventory == expected, f"Expected: {expected}, Got: {inventory}"

    def test_inventory_manager_does_nothing_when_passed_a_book_for_existing_series_that_does_not_exist():
        books_to_remove = {
            "Harry Potter": {
                "A book that does not exist": 1
            }
        }

        inventory = {
            "Harry Potter": {
                "Harry Potter and the Sorcerer's Stone": 1,
                "Harry Potter and the Chamber of Secrets": 1,
                "Harry Potter and the Prisonner of Azkaban": 1,
                "Harry Potter and the Goblet of fire": 1,
                "Harry Potter and the Order of the Phoenix": 1,
                "Harry Potter and the Half-blood Prince": 1,
                "Harry Potter and the Deathly Hallows": 1
            }
        }

        expected = {
            "Harry Potter": {
                "Harry Potter and the Sorcerer's Stone": 1,
                "Harry Potter and the Chamber of Secrets": 1,
                "Harry Potter and the Prisonner of Azkaban": 1,
                "Harry Potter and the Goblet of fire": 1,
                "Harry Potter and the Order of the Phoenix": 1,
                "Harry Potter and the Half-blood Prince": 1,
                "Harry Potter and the Deathly Hallows": 1
            }
        }

        manager = Manager(inventory)
        manager.remove_books(books_to_remove)

        assert inventory == expected, f"Expected: {expected}, Got: {inventory}"

def test_inventory_manager_can_remove_list_of_books():
    books_to_remove = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
            "Harry Potter and the Chamber of Secrets": 1,
            "Harry Potter and the Prisonner of Azkaban": 1,
            "Harry Potter and the Goblet of fire": 1,
            "Harry Potter and the Order of the Phoenix": 1,
            "Harry Potter and the Half-blood Prince": 1,
            "Harry Potter and the Deathly Hallows": 1
        }
    }

    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
            "Harry Potter and the Chamber of Secrets": 1,
            "Harry Potter and the Prisonner of Azkaban": 1,
            "Harry Potter and the Goblet of fire": 1,
            "Harry Potter and the Order of the Phoenix": 1,
            "Harry Potter and the Half-blood Prince": 1,
            "Harry Potter and the Deathly Hallows": 1
        }
    }

    expected = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 0,
            "Harry Potter and the Chamber of Secrets": 0,
            "Harry Potter and the Prisonner of Azkaban": 0,
            "Harry Potter and the Goblet of fire": 0,
            "Harry Potter and the Order of the Phoenix": 0,
            "Harry Potter and the Half-blood Prince": 0,
            "Harry Potter and the Deathly Hallows": 0
        }
    }
    manager = Manager(inventory)
    manager.remove_books(books_to_remove)

    assert inventory == expected, f"Expected: {expected}, Got: {inventory}"

def test_number_of_books_in_inventory_cannot_be_negative():
    books_to_remove = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 2,
            "Harry Potter and the Chamber of Secrets": 2,
            "Harry Potter and the Prisonner of Azkaban": 2,
            "Harry Potter and the Goblet of fire": 2,
            "Harry Potter and the Order of the Phoenix": 2,
            "Harry Potter and the Half-blood Prince": 2,
            "Harry Potter and the Deathly Hallows": 2
        }
    }

    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
            "Harry Potter and the Chamber of Secrets": 1,
            "Harry Potter and the Prisonner of Azkaban": 1,
            "Harry Potter and the Goblet of fire": 1,
            "Harry Potter and the Order of the Phoenix": 1,
            "Harry Potter and the Half-blood Prince": 1,
            "Harry Potter and the Deathly Hallows": 1
        }
    }

    expected = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 0,
            "Harry Potter and the Chamber of Secrets": 0,
            "Harry Potter and the Prisonner of Azkaban": 0,
            "Harry Potter and the Goblet of fire": 0,
            "Harry Potter and the Order of the Phoenix": 0,
            "Harry Potter and the Half-blood Prince": 0,
            "Harry Potter and the Deathly Hallows": 0
        }
    }
    manager = Manager(inventory)
    manager.remove_books(books_to_remove)

    assert inventory == expected, f"Expected: {expected}, Got: {inventory}"



def test_adding_book_not_existing_in_inventory():
    book_to_add = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
        }
    }

    inventory = {}
    expected = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1
        }
    }

    manager = Manager(inventory)
    manager.add_books(book_to_add)

    assert inventory == expected, f"Expected: {expected}, Got: {inventory}"

def test_adding_book_existing_in_inventory():
    book_to_add = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
        }
    }

    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
        }
    }

    expected = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 2
        }
    }

    manager = Manager(inventory)
    manager.add_books(book_to_add)

    assert inventory == expected, f"Expected: {expected}, Got: {inventory}"

def test_adding_multiple_copies_of_a_book_existing_in_inventory():
    book_to_add = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 20,
        }
    }

    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
        }
    }

    expected = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 21
        }
    }

    manager = Manager(inventory)
    manager.add_books(book_to_add)

    assert inventory == expected, f"Expected: {expected}, Got: {inventory}"
