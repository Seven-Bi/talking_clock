import re


def number_word_dict():
    transfer_dict = {}

    word_list_1 = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 
        'seventeen', 'eighteen', 'nineteen',
        'twenty'
    ]
    
    word_list_2 = [
        'thirty', 'fourty', 'fifty'
    ]

    for i in range(21):
        transfer_dict[str(i)] = word_list_1[i]

    count = 0
    for i in [30, 40, 50]:
        transfer_dict[str(i)] = word_list_2[count]
        count += 1

    return transfer_dict



def num_to_word(input_str):
    output_str = ''

    regex_pattern = '([0-1][0-9]|[2][0-4]):[0-5][0-9]'
    p = re.compile(regex_pattern)
    fix_len = 5
    transfer_dict = number_word_dict()

    # parameter type check
    if isinstance(input_str, str) == False:
        return '-1'

    # parameter validation(format and len check)
    if p.match(input_str) == False or len(input_str) != fix_len:
        return '-2'
    
    input_list = input_str.split(':')
    hours = input_list[0]
    mins = input_list[1]
    daytime = 'am'
    flag_code = int(hours) // 12

    if flag_code >= 1 and flag_code < 2:
        daytime = 'pm'

    if hours == '00':
        hours = '0'
    else:
        temp_hours = int(hours)
        hours = str(temp_hours % 12)

    
    hours = transfer_dict[hours]

    if int(mins) // 20 > 0 and int(mins) != 30 and int(mins) != 40 and int(mins) != 50:
        mins = transfer_dict[mins[0]+'0'] + ' ' + transfer_dict[mins[1]]
    else:
        if mins == '00':
            mins = '0'
        temp_mins = int(mins)
        mins = str(temp_mins)
        mins = transfer_dict[mins]
    output_str = 'It is '  + hours + ':' + mins + ' ' + daytime

    return output_str
