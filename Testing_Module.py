import unittest


class ListFunctions(unittest.TestCase):
    def list_pop(self):
        l = [5, 9, 4, 2, 0, 6]
        self.assertEqual(l.pop(2), 4)

    def list_index(self):
        l = [5, 9, 4, 2, 0, 6]
        self.assertNotEqual(l.index(0), 5)

    def list_index1(self):
        l = [5, 9, 4, 2, 0, 6]
        self.assertNotEqual(l.index(0), 4)

    def list_in(self):
        l = [5, 9, 4, 2, 0, 6]
        self.assertTrue(4 in l)

    def list_in1(self):
        l = [5, 9, 4, 2, 0, 6]
        self.assertFalse(10 in l)

    def list_compare(self):
        l = [5, 9, 4, 2, 0, 6]
        k = [5, 9, 4, 2, 0, 6, 7, 8]
        self.assertGreater(k, l)

    def list_compare1(self):
        l = [5, 9, 4, 2, 0, 6]
        k = [5, 9, 4, 2, 0, 6, 7, 8]
        self.assertLess(k, l)

    def int_convert(self):
        with self.assertRaises(ValueError):
            int('gh')

    def list_index_error(self):
        k = [5, 9, 4, 2, 0, 6, 7, 8]
        with self.assertRaises(IndexError):
            k.pop(9)

    def list_index_error1(self):
        k = [5, 9, 4, 2, 0, 6, 7, 8]
        with self.assertRaises(IndexError):
            k.pop(5)


if __name__ == '__main__':
    unittest.main()
