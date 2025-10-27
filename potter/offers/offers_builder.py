from potter.books_series_configurations.harry_potter import HarryPotterSeries
from potter.bundles.bundle_maker import BundleMaker
from potter.billing.biller import Biller
from potter.books_series_configurations.realm_of_the_elderlings import RealmOfTheElderlingSeries

class OffersBuilder():
    def __init__(self, inventory, biller_configuration):
        self.inventory = inventory
        self.biller_configuration = biller_configuration

    def available_offers(self):
        bundles = BundleMaker(self.inventory).get_bundles()
        offers = []

        for bundle in bundles:
            series_name = bundle["series_name"]
            content = bundle["content"]

            if series_name == "Harry Potter":
                books_config = HarryPotterSeries()
            else:
                books_config = RealmOfTheElderlingSeries()


            price = Biller(content, self.biller_configuration, books_config).bill()
            offers.append({"price": price, "books": content})

        return offers
