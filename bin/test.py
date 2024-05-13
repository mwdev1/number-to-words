import unittest
import numbers_to_words

class TestConversionCases(unittest.TestCase):
    def test_case_1(self):
        result = numbers_to_words.convert_to_words(52)
        self.assertEqual(result, "fifty-two")

    def test_case_2(self):
        result = numbers_to_words.convert_to_words(1000)
        self.assertEqual(result, "one thousand")

    def test_case_3(self):
        result = numbers_to_words.convert_to_words(101)
        self.assertEqual(result, "one hundred and one")

    def test_case_4(self):
        result = numbers_to_words.convert_to_words(352)
        self.assertEqual(result, "three hundred and fifty-two")

    def test_case_5(self):
        result = numbers_to_words.convert_to_words(12300)
        self.assertEqual(result, "twelve thousand, three hundred")

    def test_case_6(self):
        result = numbers_to_words.convert_to_words(12055)
        self.assertEqual(result, "twelve thousand and fifty-five")

    def test_case_7(self):
        result = numbers_to_words.convert_to_words(12345)
        self.assertEqual(result, "twelve thousand, three hundred and forty-five")

if __name__ == '__main__':
    unittest.main()
