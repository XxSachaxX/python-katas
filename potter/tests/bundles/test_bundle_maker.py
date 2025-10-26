from potter.bundles.bundle_maker import get_bundles

def test_with_a_single_book():
    books = ["Harry Potter and the Sorcerer's Stone"]
    expected = [["Harry Potter and the Sorcerer's Stone"]]
    result = get_bundles(books)

    assert result == expected, f"Expected: {expected}, Got: {result}"

def test_with_two_books():
    books = ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"]
    expected = [["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"]]
    result = get_bundles(books)

    assert result == expected, f"Expected: {expected}, Got: {result}"

def test_with_two_different_books_and_an_identical_one():
    books = ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Sorcerer's Stone"]
    expected = [["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets"], ["Harry Potter and the Sorcerer's Stone"]]
    result = get_bundles(books)

    assert result == expected, f"Expected: {expected}, Got: {result}"

def test_with_three_identical_books():
    books = ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Sorcerer's Stone", "Harry Potter and the Sorcerer's Stone"]
    expected = [["Harry Potter and the Sorcerer's Stone"],["Harry Potter and the Sorcerer's Stone"],["Harry Potter and the Sorcerer's Stone"]]
    result = get_bundles(books)

    assert result == expected, f"Expected: {expected}, Got: {result}"

def test_with_three_other_identical_books():
    books = ["Harry Potter and the Chamber of Secrets", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Chamber of Secrets"]
    expected = [["Harry Potter and the Chamber of Secrets"],["Harry Potter and the Chamber of Secrets"],["Harry Potter and the Chamber of Secrets"]]
    result = get_bundles(books)

    assert result == expected, f"Expected: {expected}, Got: {result}"
