import sys
import unittest
import json
sys.path.append('..')
from app.talking import number_word_dict, num_to_word


class TestTalkingClock(unittest.TestCase):
    def test_number_word_dict(self):
        data = {}
        with open('test_cases.json') as json_file:
            data = json.load(json_file)
            self.assertEqual(number_word_dict(), data['dict_data'])

    def test_num_to_word(self):
        with open('test_cases.json') as json_file:
            data = json.load(json_file)
            # test different numeric time and format
            for k, v in data['time_data_test'].items():
                self.assertEqual(num_to_word(k), v)
            # test wrong parameters' type
            for k, v in data['time_data_exp_test'].items():
                self.assertEqual(num_to_word(k), v)
            self.assertEqual(num_to_word(6088), '-1')

if __name__ == '__main__':
    unittest.main()