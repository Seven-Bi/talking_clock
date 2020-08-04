import unittest
import json
from talking_clock.src.app.talking_clock import number_word_dict


class TestTalkingClock(unittest.TestCase):
    def test_number_word_dict(self):
        data = {}
        with open('test_cases.json') as json_file:
            data = json.load(json_file)
            self.assertEqual(number_word_dict(), data['dict_data'])

if __name__ == '__main__':
    unittest.main()