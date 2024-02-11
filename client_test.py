import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    def test_getDataPoint_calculatePrice(self):
         new_quotes = [
      {'top_ask': {'price': 122.5, 'size': 40}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.75, 'size': 100}, 'id': '0.109974697771', 'stock': 'GHI'},
      {'top_ask': {'price': 119.3, 'size': 10}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 118.1, 'size': 70}, 'id': '0.109974697771', 'stock': 'JKL'}
    ]



  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
