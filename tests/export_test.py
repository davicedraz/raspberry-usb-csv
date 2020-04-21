import sys
import unittest

from export import export

class TestExport(unittest.TestCase):

    def setUp(self):
        self.data = {
            "Date": "8/19/2014",
            "Open": 585.002622,
            "High": 587.342658,
            "Low": 584.002627,
            "Close": 586.862643,
            "Volume": 978600,
            "Adj": 586.862643
        }

if __name__ == '__main__':
    export.write_header(data)
    export.write_data(data)
