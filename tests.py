from unittest import TestCase, main
from state import State

class StateTests(TestCase):
    def test_remove_letter(self):
        state = State(['right', 'wrong', 'cools', 'idiot'])
        self.assertEqual(len(state.words), 4)

        state.remove_letter('r')
        self.assertEqual(len(state.words), 2)

    def test_correct_pos(self):
        state = State(['goods', 'baggy', 'hippe', 'dumbo'])
        self.assertEqual(len(state.words), 4)

        state.correct_pos('g', 0)
        self.assertEqual(len(state.words), 1)

    def test_wrong_pos(self):
        state = State(['goods', 'baggy', 'higge', 'dumbo'])
        self.assertEqual(len(state.words), 4)

        state.wrong_pos('g', 0)
        self.assertEqual(len(state.words), 2)

if __name__ == "__main__":
    main()