from potter.inventory.manager import Manager

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
