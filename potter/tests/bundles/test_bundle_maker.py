from potter.bundles.bundle_maker import BundleMaker

def test_with_a_single_book():
    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
            "Harry Potter and the Chamber of Secrets": 0,
            "Harry Potter and the Prisonner of Azkaban": 0,
            "Harry Potter and the Goblet of fire": 0,
            "Harry Potter and the Order of the Phoenix": 0,
            "Harry Potter and the Half-blood Prince": 0,
            "Harry Potter and the Deathly Hallows": 0

        }
    }
    expected = [["Harry Potter and the Sorcerer's Stone"]]

    bundle_maker = BundleMaker(inventory)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_books():
    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
            "Harry Potter and the Chamber of Secrets": 1,
            "Harry Potter and the Prisonner of Azkaban": 0,
            "Harry Potter and the Goblet of fire": 0,
            "Harry Potter and the Order of the Phoenix": 0,
            "Harry Potter and the Half-blood Prince": 0,
            "Harry Potter and the Deathly Hallows": 0

        }
    }

    expected = [["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"]]
    bundle_maker = BundleMaker(inventory)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_different_books_and_an_identical_one():
    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 2,
            "Harry Potter and the Chamber of Secrets": 1,
            "Harry Potter and the Prisonner of Azkaban": 0,
            "Harry Potter and the Goblet of fire": 0,
            "Harry Potter and the Order of the Phoenix": 0,
            "Harry Potter and the Half-blood Prince": 0,
            "Harry Potter and the Deathly Hallows": 0

        }
    }

    expected = [["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"], ["Harry Potter and the Sorcerer's Stone"]]
    bundle_maker = BundleMaker(inventory)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_three_identical_books():
    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 3,
            "Harry Potter and the Chamber of Secrets": 0,
            "Harry Potter and the Prisonner of Azkaban": 0,
            "Harry Potter and the Goblet of fire": 0,
            "Harry Potter and the Order of the Phoenix": 0,
            "Harry Potter and the Half-blood Prince": 0,
            "Harry Potter and the Deathly Hallows": 0

        }
    }

    expected = [["Harry Potter and the Sorcerer's Stone"],["Harry Potter and the Sorcerer's Stone"],["Harry Potter and the Sorcerer's Stone"]]
    bundle_maker = BundleMaker(inventory)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_three_other_identical_books():
    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 0,
            "Harry Potter and the Chamber of Secrets": 3,
            "Harry Potter and the Prisonner of Azkaban": 0,
            "Harry Potter and the Goblet of fire": 0,
            "Harry Potter and the Order of the Phoenix": 0,
            "Harry Potter and the Half-blood Prince": 0,
            "Harry Potter and the Deathly Hallows": 0

        }
    }

    expected = [["Harry Potter and the Chamber of Secrets"],["Harry Potter and the Chamber of Secrets"],["Harry Potter and the Chamber of Secrets"]]
    bundle_maker = BundleMaker(inventory)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_sets_of_unique_books():
    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 2,
            "Harry Potter and the Chamber of Secrets": 2,
            "Harry Potter and the Prisonner of Azkaban": 0,
            "Harry Potter and the Goblet of fire": 0,
            "Harry Potter and the Order of the Phoenix": 0,
            "Harry Potter and the Half-blood Prince": 0,
            "Harry Potter and the Deathly Hallows": 0

        }
    }

    expected = [["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"], ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"]]

    bundle_maker = BundleMaker(inventory)
    result = bundle_maker.get_bundles()
    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_sets_of_unique_books_and_a_book_left_alone():
    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 3,
            "Harry Potter and the Chamber of Secrets": 2,
            "Harry Potter and the Prisonner of Azkaban": 0,
            "Harry Potter and the Goblet of fire": 0,
            "Harry Potter and the Order of the Phoenix": 0,
            "Harry Potter and the Half-blood Prince": 0,
            "Harry Potter and the Deathly Hallows": 0

        }
    }

    expected = [["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"], ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"],["Harry Potter and the Sorcerer's Stone"]]

    bundle_maker = BundleMaker(inventory)
    result = bundle_maker.get_bundles()
    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_sets_of_unique_books_with_different_length():
    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 3,
            "Harry Potter and the Chamber of Secrets": 2,
            "Harry Potter and the Prisonner of Azkaban": 1,
            "Harry Potter and the Goblet of fire": 1,
            "Harry Potter and the Order of the Phoenix": 1,
            "Harry Potter and the Half-blood Prince": 0,
            "Harry Potter and the Deathly Hallows": 0

        }
    }

    expected = [["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisonner of Azkaban", "Harry Potter and the Goblet of fire", "Harry Potter and the Order of the Phoenix"], ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"],["Harry Potter and the Sorcerer's Stone"]]

    bundle_maker = BundleMaker(inventory)
    result = bundle_maker.get_bundles()
    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_one_book_from_two_different_series():
    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
            "Harry Potter and the Chamber of Secrets": 0,
            "Harry Potter and the Prisonner of Azkaban": 0,
            "Harry Potter and the Goblet of fire": 0,
            "Harry Potter and the Order of the Phoenix": 0,
            "Harry Potter and the Half-blood Prince": 0,
            "Harry Potter and the Deathly Hallows": 0

        },
        "Realm of the elderlings": {
            "Assassin's Apprentice": 1,
            "Royal Assassin": 0,
            "Assassin's Quest": 0,
            "Fool's Errand": 0,
            "Golden Fool": 0,
            "Fool's Fate": 0,
            "The Rain Wilds Chronicles: Dragon Keeper": 0,
            "Dragon Haven": 0,
            "City of Dragons": 0,
            "Blood of Dragons": 0,
            "Fitz and the Fool Trilogy: Fool's Assassin": 0,
            "Fool's Quest": 0,
            "Assassin's Fate": 0
        }
    }

    expected = [["Harry Potter and the Sorcerer's Stone"],["Assassin's Apprentice"]]
    bundle_maker = BundleMaker(inventory)
    result = bundle_maker.get_bundles()
    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_different_complete_series():
    inventory = {
        "Harry Potter": {
            "Harry Potter and the Sorcerer's Stone": 1,
            "Harry Potter and the Chamber of Secrets": 1,
            "Harry Potter and the Prisonner of Azkaban": 1,
            "Harry Potter and the Goblet of fire": 1,
            "Harry Potter and the Order of the Phoenix": 1,
            "Harry Potter and the Half-blood Prince": 1,
            "Harry Potter and the Deathly Hallows": 1

        },
        "Realm of the elderlings": {
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

    harry_potter_full_bundle = [
        "Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisonner of Azkaban",
        "Harry Potter and the Goblet of fire", "Harry Potter and the Order of the Phoenix", "Harry Potter and the Half-blood Prince", "Harry Potter and the Deathly Hallows"
    ]
    realm_of_the_underlings_full_bundle = [
        "Assassin's Apprentice",
        "Royal Assassin",
        "Assassin's Quest",
        "Fool's Errand",
        "Golden Fool",
        "Fool's Fate",
        "The Rain Wilds Chronicles: Dragon Keeper",
        "Dragon Haven",
        "City of Dragons",
        "Blood of Dragons",
        "Fitz and the Fool Trilogy: Fool's Assassin",
        "Fool's Quest",
        "Assassin's Fate"
    ]
    expected = [harry_potter_full_bundle,realm_of_the_underlings_full_bundle]
    bundle_maker = BundleMaker(inventory)
    result = bundle_maker.get_bundles()
    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"
