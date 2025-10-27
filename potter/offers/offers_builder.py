from potter.books_series_configurations.harry_potter import HarryPotterSeries
from potter.bundles.bundle_maker import BundleMaker
from potter.billing.biller import Biller
from potter.books_series_configurations.realm_of_the_elderlings import RealmOfTheElderlingsSeries

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


            books_config = self.__get_books_series_configuration(series_name)


            price = Biller(content, self.biller_configuration, books_config).bill()
            offers.append({"price": price, "books": content})

        return offers

    def __get_books_series_configuration(self, series_name):
        config_name = series_name.title().replace(" ", "") + "Series"
        cls = globals()[config_name]

        return cls()
