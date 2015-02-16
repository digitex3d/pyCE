__author__ = 'Giuseppe Federico'

import unittest
from environment.CardStack import *
from environment.Card import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.deck = CardStack([Card(1),Card(2),Card(3),Card(4)])

    def test_shuffle(self):
        tmp = self.deck.copy()
        self.deck.shuffle()
        self.assertNotEqual(str(tmp), str(self.deck))

    def test_size(self):
        self.assertEqual(4, self.deck.size())

    def test_getLast(self):
        self.assertEqual(4, self.deck.getLast().value)


if __name__ == '__main__':
    unittest.main()
