from unittest import TestCase

import main


class Test(TestCase):
    def test_is_balanced_no_interest(self):
        self.assertEqual(main.isBalanced("twtw"), True)

    def test_balanced_symbol_of_interest(self):
        self.assertEqual(main.isBalanced("[{}]"), True)

    def test_is_unbalanced_opening(self):
        self.assertEqual(main.isBalanced("{}[[]{}"), False)

    def test_is_unbalanced_closing(self):
        self.assertEqual(main.isBalanced("[[]]]"), False)

    def test_is_unbalanced_unarranged(self):
        self.assertEqual(main.isBalanced("[{]}"), False)

    def test_is_unbalanced_unarranged_closing(self):
        self.assertEqual(main.isBalanced("{[{]}"), False)

    def test_is_unbalanced_unarranged_opening(self):
        self.assertEqual(main.isBalanced("[{]}]"), False)
