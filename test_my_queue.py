import unittest
from my_queue import Queue

class TestMyQueue(unittest.TestCase):

    def test_enqueue(self):
        newQueue = Queue()
        self.assertEqual(newQueue.enqueue('A'), ['A'])

    def test_dequeue(self):
        newQueue = Queue()
        newQueue.enqueue('A')
        self.assertEqual(newQueue.dequeue(), [])

    def test_peek_returns_item(self):
        newQueue = Queue()
        newQueue.enqueue('A')
        self.assertIs(newQueue.peek(), 'A')

    def test_peek_does_not_return_item(self):
        newQueue = Queue()
        self.assertIsNone(newQueue.peek())

    def test_empty_true(self):
        newQueue = Queue()
        self.assertTrue(newQueue.empty())

    def test_empty_false(self):
        newQueue = Queue()
        newQueue.enqueue('A')
        self.assertFalse(newQueue.empty())

    def test_front_has_item(self):
        newQueue = Queue()
        newQueue.enqueue('A')
        newQueue.enqueue('B')
        self.assertIsNotNone(newQueue.front())

    def test_front_does_not_have_item(self):
        newQueue = Queue()
        self.assertIsNone(newQueue.front())

    def test_rear_has_item(self):
        newQueue = Queue()
        newQueue.enqueue('A')
        newQueue.enqueue('B')
        self.assertIsNotNone(newQueue.rear())
        
    def test_rear_does_not_have_item(self):
        newQueue = Queue()
        self.assertIsNone(newQueue.rear())

    def test_size(self):
        newQueue = Queue()
        newQueue.enqueue('A')
        newQueue.enqueue('B')
        newQueue.enqueue('2')
        self.assertEqual(newQueue.size(), 3)

if __name__ == '__main__':
    unittest.main()