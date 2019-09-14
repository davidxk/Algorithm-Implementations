import unittest
import random
from rna_secondary_structure import *

class TestRNASecondaryStructure(unittest.TestCase):
    def __gen_case__(self):
        bases = "AUCG"
        return str().join(random.choice(bases) for i in range(50))

    def testTableFilling(self):
        for i in range(100):
            case = self.__gen_case__()
            max1 = rna_secondary_structure(case)
            max2 = rna_secondary_structure_memo(case)
            self.assertEqual(max1, max2)

if __name__ == "__main__":
    unittest.main()
