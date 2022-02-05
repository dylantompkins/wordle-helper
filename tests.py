from unittest import TestCase, main
from state import State

class StateTests(TestCase):
    def test_remove_letter(self):
        state = State(['right', 'wrong', 'cools', 'idiot'])
        self.assertEqual(len(state.words), 4)

        state.remove_letter('r')
        self.assertEqual(len(state.words), 2)


if __name__ == "__main__":
    main()