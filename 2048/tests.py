import unittest
from main import get_number_from_index, get_empty_list, get_index_from_number


class Test_2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_number_from_index(1, 2), 7)

    def test_2(self):
        self.assertEqual(get_number_from_index(3, 3), 16)

    def test_3(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_4(self):
        a = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [1, 1, 2, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_4(self):
        a = []
        mas = [
            [1, 1, 2, 4],
            [2, 4, 5, 6],
            [4, 2, 6, 5],
            [1, 1, 1, 6],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_5(self):
        self.assertEqual(get_index_from_number(7), (1, 2))

    def test_6(self):
        self.assertEqual(get_index_from_number(16), (3, 3))


        if __name__ == 'main':
            unittest.main()
