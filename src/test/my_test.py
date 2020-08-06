import sys
import os
import unittest
import json
sys.path.append('..')
from src.app.talking import number_word_dict, num_to_word


class TestTalkingClock(unittest.TestCase):
    '''
    Test case 1
    test_number_word_dict() reads test data <dict_data> from test_cases.json file 
    comparing with number_word_dict() return data, check if there is correct dict
    for later use

    Test case 2
    test_num_to_word() reads data <time_data_test> and <time_data_error_test>, the former
    is for checking if the function already covered all cases to making sure all the numeric
    time data can be translated to human words
    the latter is for checking if the wrong format and type data get in, see if function can catch 
    and report specific error code
    '''

    def test_number_word_dict(self):
        data = {}
        with open(os.path.abspath('test/test_cases.json')) as json_file:
            data = json.load(json_file)
            self.assertEqual(number_word_dict(), data['dict_data'])

    def test_num_to_word(self):
        with open(os.path.abspath('test/test_cases.json')) as json_file:
            data = json.load(json_file)

            # test different numeric time and format
            for k, v in data['time_data_test'].items():
                self.assertEqual(num_to_word(k), v)

            # test wrong parameters
            for k, v in data['time_data_error_test'].items():
                self.assertEqual(num_to_word(k), v)
            self.assertEqual(num_to_word(6088), '-1')

unittest.main()

# if __name__ == '__main__':
#     unittest.main()
#     start()