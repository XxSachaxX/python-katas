from potter.cash.register import Register
from potter.biller_configurations.default import DefaultBillerConfiguration

default_configuration = DefaultBillerConfiguration()

def test_has_cash_float():
    initial_cash_float = 20000
    initial_inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
        }
    }
    register = Register(initial_cash_float, initial_inventory, default_configuration)
    actual_cash_float = register.cash_float

    assert actual_cash_float == 20000, f"Expected register to have cash float {initial_cash_float}, but has {actual_cash_float}"

def test_has_inventory():
    initial_inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
        }
    }

    initial_cash_float = 1000
    register = Register(initial_cash_float, initial_inventory, default_configuration)
    actual_inventory = register.inventory

    assert actual_inventory == initial_inventory, f"Expected inventory: {initial_inventory}, got: {actual_inventory}"

def test_cash_in_a_cart_with_a_single_book():
    initial_inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
        }
    }

    initial_cash_float = 1000
    register = Register(initial_cash_float, initial_inventory, default_configuration)
    customer_cart = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
        }
    }

    expected_inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 0,
        }
    }
    expected_cash_float = 992

    register.cash_in(customer_cart)
    assert register.inventory == initial_inventory, f"Expected inventory: {expected_inventory}, got: {register.inventory}"
    assert register.cash_float == expected_cash_float, f"Expected register to have cash float {expected_cash_float}, but has {register.cash_float}"


def test_cash_in_a_cart_with_many_books_from_same_series():
    initial_inventory = {
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

    initial_cash_float = 1000
    register = Register(initial_cash_float, initial_inventory, default_configuration)
    customer_cart = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
            "Harry Potter and the Prisonner of Azkaban": 1,
            "Harry Potter and the Order of the Phoenix": 1,
            "Harry Potter and the Half-blood Prince": 1,
        }
    }

    expected_inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 0,
            "Harry Potter and the Chamber of Secrets": 1,
            "Harry Potter and the Prisonner of Azkaban": 0,
            "Harry Potter and the Goblet of fire": 1,
            "Harry Potter and the Order of the Phoenix": 0,
            "Harry Potter and the Half-blood Prince": 0,
            "Harry Potter and the Deathly Hallows": 1
        }
    }
    expected_cash_float = 974.40

    register.cash_in(customer_cart)
    assert register.inventory == initial_inventory, f"Expected inventory: {expected_inventory}, got: {register.inventory}"
    assert register.cash_float == expected_cash_float, f"Expected register to have cash float {expected_cash_float}, but has {register.cash_float}"


def test_cash_in_a_cart_with_many_books_from_different_series():
    initial_inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
            "Harry Potter and the Chamber of Secrets": 1,
            "Harry Potter and the Prisonner of Azkaban": 1,
            "Harry Potter and the Goblet of fire": 1,
            "Harry Potter and the Order of the Phoenix": 1,
            "Harry Potter and the Half-blood Prince": 1,
            "Harry Potter and the Deathly Hallows": 1

        },
        "Realm Of The Elderlings": {
            "Assassin's Apprentice": 1,
            "Royal Assassin": 1,
            "Assassin's Quest": 1,
            "Fool's Errand": 1,
            "Golden Fool": 1,
            "Fool's Fate": 1,
            "The Rain Wilds Chronicles: Dragon Keeper": 1,
            "Dragon Haven": 1,
            "City of Dragons": 1,
            "Blood of Dragons": 1,
            "Fitz and the Fool Trilogy: Fool's Assassin": 1,
            "Fool's Quest": 1,
            "Assassin's Fate": 1
        }
    }

    initial_cash_float = 1000
    register = Register(initial_cash_float, initial_inventory, default_configuration)
    customer_cart = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
            "Harry Potter and the Prisonner of Azkaban": 1,
            "Harry Potter and the Order of the Phoenix": 1,
            "Harry Potter and the Half-blood Prince": 1,
        },
        "Realm Of The Elderlings": {
            "Assassin's Quest": 1,
            "Fool's Errand": 1,
            "Golden Fool": 1,
            "Fool's Fate": 1,
        }
    }

    expected_inventory  = initial_inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 0,
            "Harry Potter and the Chamber of Secrets": 1,
            "Harry Potter and the Prisonner of Azkaban": 0,
            "Harry Potter and the Goblet of fire": 1,
            "Harry Potter and the Order of the Phoenix": 0,
            "Harry Potter and the Half-blood Prince": 0,
            "Harry Potter and the Deathly Hallows": 1

        },
        "Realm Of The Elderlings": {
            "Assassin's Apprentice": 1,
            "Royal Assassin": 1,
            "Assassin's Quest": 0,
            "Fool's Errand": 0,
            "Golden Fool": 0,
            "Fool's Fate": 0,
            "The Rain Wilds Chronicles: Dragon Keeper": 1,
            "Dragon Haven": 1,
            "City of Dragons": 1,
            "Blood of Dragons": 1,
            "Fitz and the Fool Trilogy: Fool's Assassin": 1,
            "Fool's Quest": 1,
            "Assassin's Fate": 1
        }
    }
    expected_cash_float = 948.8

    register.cash_in(customer_cart)
    assert register.inventory == initial_inventory, f"Expected inventory: {expected_inventory}, got: {register.inventory}"
    assert register.cash_float == expected_cash_float, f"Expected register to have cash float {expected_cash_float}, but has {register.cash_float}"
