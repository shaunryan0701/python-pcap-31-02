import math

def halve_string(input_string):
    first_half = input_string[: math.ceil(len(input_string)/2)]
    second_half = input_string[math.ceil(len(input_string)/2) :]
    return (first_half, second_half)
