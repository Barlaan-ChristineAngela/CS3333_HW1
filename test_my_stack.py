import unittest
from my_stack import Stack

class TestMyStack(unittest.TestCase):

    def test_push(self):
        myStack = Stack()
        self.assertEqual(myStack.push('A'), ['A'])

    def test_pop(self):
        myStack = Stack()
        myStack.push('A')
        self.assertEqual(myStack.pop(), [])

    def test_empty_true(self):
        myStack = Stack()
        self.assertTrue(myStack.empty())
        
    def test_empty_false(self):
        myStack = Stack()
        myStack.push('A')
        self.assertFalse(myStack.empty())

    def test_peek_has_item_in_stack(self):
        myStack = Stack()
        myStack.push('A')
        self.assertIsNotNone(myStack.peek())

    def test_peek_does_not_have_item_in_stack(self):
        myStack = Stack()
        self.assertIsNone(myStack.peek())

    def test_size(self):
        myStack = Stack()
        myStack.push('apples')
        myStack.push('oranges')
        self.assertEqual(myStack.size(), 2)

if __name__ == '__main__':
    unittest.main()