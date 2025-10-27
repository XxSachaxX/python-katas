from potter.bundles.bundle_maker import BundleMaker

# Tests with a single series
chosen_series = "Harry Potter"
def test_with_a_single_book():
    inventory = {
        chosen_series: {
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

    bundle_maker = BundleMaker(inventory, chosen_series)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_books():
    inventory = {
        chosen_series: {
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
    bundle_maker = BundleMaker(inventory, chosen_series)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_different_books_and_an_identical_one():
    inventory = {
        chosen_series: {
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
    bundle_maker = BundleMaker(inventory, chosen_series)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_three_identical_books():
    inventory = {
        chosen_series: {
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
    bundle_maker = BundleMaker(inventory, chosen_series)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_three_other_identical_books():
    inventory = {
        chosen_series: {
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
    bundle_maker = BundleMaker(inventory, chosen_series)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_sets_of_unique_books():
    inventory = {
        chosen_series: {
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

    bundle_maker = BundleMaker(inventory, chosen_series)
    result = bundle_maker.get_bundles()
    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_sets_of_unique_books_and_a_book_left_alone():
    inventory = {
        chosen_series: {
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

    bundle_maker = BundleMaker(inventory, chosen_series)
    result = bundle_maker.get_bundles()
    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_sets_of_unique_books_with_different_length():
    inventory = {
        chosen_series: {
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

    bundle_maker = BundleMaker(inventory, chosen_series)
    result = bundle_maker.get_bundles()
    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"
