from potter.offers.offers_builder import OffersBuilder
from potter.biller_configurations.default import DefaultBillerConfiguration

biller_configuration = DefaultBillerConfiguration()

def test_with_empty_inventory():
    inventory = {}
    offers_builder = OffersBuilder(inventory, biller_configuration)
    expected_offers = []
    actual_offers = offers_builder.available_offers()

    assert sorted(actual_offers) == sorted(expected_offers), f"Expected: {expected_offers}, Got: {actual_offers}"

def test_inventory_with_two_full_series():
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

    offers_builder = OffersBuilder(inventory, biller_configuration)
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

    expected_offers = [
        {"price": 42, "books": harry_potter_full_bundle},
        {"price": 78, "books": realm_of_the_underlings_full_bundle}
    ]
    actual_offers = offers_builder.available_offers()

    assert_same_dicts(expected_offers, actual_offers), f"Expected: {expected_offers}, Got: {actual_offers}"


def assert_same_dicts(list1, list2):
    assert len(list1) == len(list2)
    for item in list1:
        assert item in list2
