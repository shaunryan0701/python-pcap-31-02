import string_utils

def halve_strings(string_list):
    halved_strings = []
    for string_element in string_list:
        halved_strings.append(string_utils.halve_string(string_element))

    return halved_strings
