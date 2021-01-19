#######################
# Test Processing II  #
#######################


def digits_to_words(input_string):
    result_list = []
    text_list = ["zero","one","two","three","four","five","six","seven","eight", "nine"]
    for string_char in input_string:
        if string_char.isdigit():
            result_list.append(text_list[int(string_char)])

    digit_string = None
    if len(result_list) > 0:
        digit_string = " ".join(result_list)
    else:
        digit_string = ""        
    return digit_string

"""
컴퓨터 프로그래밍에 많은 명명 규칙이 있지만, 두 규칙이 특히 흔히 쓰입니다. 
첫번째로는, 변수 이름을 'underscore'로 나눠준다거나, (ex. under_score_variable)
두번째로는, 변수 이름을 대소문자 구별해 구분자 (delimiter)없이 쓰는 경우가 있습니다. 
이 두번째의 경우에는 첫번째 단어는 소문자로, 그 후에 오는 단어들의 첫번째 글자들은 대문자로 쓰입니다 (ex. camelCaseVariable). 
"""


def to_camel_case(underscore_str):
    str_list = underscore_str.split('_')
    str_filtered_list = [string for string in str_list if string != ""]
    str_len = len(str_filtered_list)
    if str_len > 0:
        str_filtered_list[0] = str_filtered_list[0].lower()
        for i in range(1,str_len):
            str_filtered_list[i] = str_filtered_list[i].capitalize()
        camelcase_str = "".join(str_filtered_list)
    else:
        camelcase_str = ""
    return camelcase_str
