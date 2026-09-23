import unittest
from src.priority import normalise_priority


class PriorityTests(unittest.TestCase):
    def test_canonical_values(self):
        for value in ("P0", "P1", "P2", "P3"):
            with self.subTest(value=value):
                self.assertEqual(normalise_priority(value), value)

    def test_lowercase(self):
        self.assertEqual(normalise_priority("p1"), "P1")

    def test_surrounding_whitespace(self):
        self.assertEqual(normalise_priority("  P2\n"), "P2")

    def test_combined_case_and_whitespace(self):
        self.assertEqual(normalise_priority(" p0 "), "P0")

    def test_unknown_strings(self):
        for value in ("P4", "urgent", "p 1", "P01"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    normalise_priority(value)

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            normalise_priority("")

    def test_non_strings(self):
        for value in (None, 1, True, ["P1"]):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    normalise_priority(value)


if __name__ == "__main__":
    unittest.main()
