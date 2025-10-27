from potter.bundles.bundle_maker import BundleMaker

def test_with_a_single_book():
    books = ["Harry Potter and the Sorcerer's Stone"]
    expected = [["Harry Potter and the Sorcerer's Stone"]]

    bundle_maker = BundleMaker(books)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_books():
    books = ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"]
    expected = [["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"]]
    bundle_maker = BundleMaker(books)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_different_books_and_an_identical_one():
    books = ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Sorcerer's Stone"]
    expected = [["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"], ["Harry Potter and the Sorcerer's Stone"]]
    bundle_maker = BundleMaker(books)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_three_identical_books():
    books = ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Sorcerer's Stone", "Harry Potter and the Sorcerer's Stone"]
    expected = [["Harry Potter and the Sorcerer's Stone"],["Harry Potter and the Sorcerer's Stone"],["Harry Potter and the Sorcerer's Stone"]]
    bundle_maker = BundleMaker(books)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_three_other_identical_books():
    books = ["Harry Potter and the Chamber of Secrets", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Chamber of Secrets"]
    expected = [["Harry Potter and the Chamber of Secrets"],["Harry Potter and the Chamber of Secrets"],["Harry Potter and the Chamber of Secrets"]]
    bundle_maker = BundleMaker(books)
    result = bundle_maker.get_bundles()

    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_sets_of_unique_books():
    books = ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Chamber of Secrets"]
    expected = [["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"], ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"]]

    bundle_maker = BundleMaker(books)
    result = bundle_maker.get_bundles()
    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_sets_of_unique_books_and_a_book_left_alone():
    books = ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Sorcerer's Stone"]
    expected = [["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"], ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"],["Harry Potter and the Sorcerer's Stone"]]

    bundle_maker = BundleMaker(books)
    result = bundle_maker.get_bundles()
    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"

def test_with_two_sets_of_unique_books_with_different_length():
    books = ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Sorcerer's Stone", "Harry Potter and the Prisonner of Azkaban", "Harry Potter and the Goblet of fire", "Harry Potter and the Order of the Phoenix"]
    expected = [["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisonner of Azkaban", "Harry Potter and the Goblet of fire", "Harry Potter and the Order of the Phoenix"], ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"],["Harry Potter and the Sorcerer's Stone"]]

    bundle_maker = BundleMaker(books)
    result = bundle_maker.get_bundles()
    assert sorted(result) == sorted(expected), f"Expected: {expected}, Got: {result}"
