from unittest import TestCase

from src.main import Imprimante


class TestImprimante(TestCase):

    # [9,2,4,5,6,8,9,10,14,20]
    def test_imprimer(self):
        imprimante = Imprimante("laser")
        self.assertEqual(imprimante.imprimer([9, 2, 4, 5, 6, 8, 9, 10, 14, 20]),
                         "2;4-6;8-10;14;20")
        self.assertEqual(imprimante.imprimer([18, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 665544, 665545, 665547]),
                         "987-1001;665544-665545;665547")
        self.assertEqual(imprimante.imprimer([8, 1, 52, 64, 65, 66, 999998, 999999, 1000000]),
                         "1;52;64-66;999998-1000000")

