import unittest
from my_list import List

class TestMyList(unittest.TestCase):

    def test_append(self):
        newList = List()
        self.assertEqual(newList.append('A'), ['A'])
 
    def test_copy(self):
        newList = List()
        self.assertIsNotNone(newList.copy())

    def test_clear(self):
        newList = List()
        newList.append('A')
        self.assertEqual(newList.clear(), [])

    def test_count_has_value(self):
        newList = List()
        newList.append('A')
        newList.append('A')
        self.assertEqual(newList.count('A'), 2)

    def test_count_does_not_have_value(self):
        newList = List()
        newList.append('A')
        self.assertEqual(newList.count('B'), 0)

    def test_extend(self):
        newList = List()
        newList.append('A')
        newList.append('B')

        otherList = [1, 2, 3]

        self.assertEqual(newList.extend(otherList), ['A', 'B', 1, 2, 3])

    def test_index(self):
        newList = List()
        newList.append('A')
        newList.append('B')
        self.assertEqual(newList.index('B'), 1)

    def test_insert(self):
        newList = List()
        newList.append('A')
        newList.append('B')
        self.assertEqual(newList.insert(1, 'apple'), ['A', 'apple', 'B'])

    def test_pop(self):
        newList = List()
        newList.append('A')
        newList.append('B')
        self.assertEqual(newList.pop(1), ['A'])

    def test_remove(self):
        newList = List()
        newList.append('A')
        newList.append('B')
        self.assertEqual(newList.remove('A'), ['B'])

    def test_reverse(self):
        newList = List()
        newList.append('A')
        newList.append('B')
        newList.append('C')
        self.assertEqual(newList.reverse(), ['C', 'B', 'A'])

    def test_sort(self):
        newList = List()
        newList.append('purple')
        newList.append('white')
        newList.append('brown')
        self.assertEqual(newList.sort(), ['brown', 'purple', 'white'])

    def test_get_min(self):
        newList = List()
        newList.append(1)
        newList.append(2)
        newList.append(3)
        self.assertEqual(newList.get_min(), 1)

    def test_get_max(self):
        newList = List()
        newList.append(1)
        newList.append(2)
        newList.append(3)
        self.assertEqual(newList.get_max(), 3)
                    
if __name__ == '__main__':
    unittest.main()
