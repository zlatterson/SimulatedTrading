from time import sleep
import unittest
from models.stock import Stock
from services.stock_service import StockService

class TestStock(unittest.TestCase):
    def setUp(self):
        self.stock = StockService.make_stock("AMZN")

    def test_stock_can_be_made(self):
        self.assertEqual(self.stock.summary, "Amazon.com, Inc. engages in the retail sale of consumer products and subscriptions in North America and internationally. The company operates through three segments: North America, International, and Amazon Web Services (AWS). It sells merchandise and content purchased for resale from third-party sellers through physical and online stores. The company also manufactures and sells electronic devices, including Kindle, Fire tablets, Fire TVs, Rings, and Echo and other devices; provides Kindle Direct Publishing, an online service that allows independent authors and publishers to make their books available in the Kindle Store; and develops and produces media content. In addition, it offers programs that enable sellers to sell their products on its websites, as well as its stores; and programs that allow authors, musicians, filmmakers, Twitch streamers, skill and app developers, and others to publish and sell content. Further, the company provides compute, storage, database, analytics, machine learning, and other services, as well as fulfillment, advertising, publishing, and digital content subscriptions. Additionally, it offers Amazon Prime, a membership program, which provides free shipping of various items; access to streaming of movies and series; and other services. The company serves consumers, sellers, developers, enterprises, and content creators. Amazon.com, Inc. was incorporated in 1994 and is headquartered in Seattle, Washington.")

    def test_stock_price_can_be_updated_with_method(self):
        first_price = self.stock.current_price
        sleep(0.7)
        self.stock.fetch_price()
        self.assertNotEqual(first_price, self.stock.current_price)

    def test_new_stock_can_be_made(self):
        stock2 = StockService.make_stock("DNN")
        self.assertTrue(self.stock.current_price > stock2.current_price)
