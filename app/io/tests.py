import unittest
import pandas as pd
from input import read_text_with_opportunities_python, read_with_library_pandas

class TestReadTextWithOpportunitiesPython(unittest.TestCase):
    def setUp(self):
        with open("data/input.txt", "w") as f:
            f.write("Hello from input.txt!")

    def test_read_returns_string(self):
        result = read_text_with_opportunities_python()
        self.assertIsInstance(result, str)

    def test_read_contains_expected_text(self):
        result = read_text_with_opportunities_python()
        self.assertIn("Hello from input.txt!", result)

    def test_read_not_empty(self):
        result = read_text_with_opportunities_python()
        self.assertTrue(len(result.strip()) > 0)


class TestReadWithLibraryPandas(unittest.TestCase):
    def setUp(self):
        df = pd.DataFrame({
            "Name": ["Alice", "Bob"],
            "Age": [25, 30]
        })
        df.to_csv("data/input.csv", index=False)

    def test_read_returns_string(self):
        result = read_with_library_pandas()
        self.assertIsInstance(result, str)

    def test_read_contains_column_name(self):
        result = read_with_library_pandas()
        self.assertIn("Name", result)

    def test_read_contains_data(self):
        result = read_with_library_pandas()
        self.assertIn("Alice", result)

if __name__ == '__main__':
    unittest.main()
