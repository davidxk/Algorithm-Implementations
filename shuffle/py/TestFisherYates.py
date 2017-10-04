import unittest
from fisher_yates import fisher_yates
from fisher_yates import fisher_yates_front

class TestFisherYates(unittest.TestCase):
    def testFisherYates(self):
        array = range(100)
        fisher_yates(array)

    def testFisherYatesFront(self):
        array = range(100)
        fisher_yates_front(array)

if __name__ == "__main__":
    unittest.main()
