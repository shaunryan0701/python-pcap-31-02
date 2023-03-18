# import strings_utils

# quotes = ['Being happy never goes out of style.',
# 'Life is either a great adventure or nothing.',
# 'All you need in this life is ignorance and confidence; then success is sure.',
# 'All your life, you will be faced with a choice. You can choose love or hate... I choose love.',
# 'The time is always right to do what is right.']

# print(strings_utils.halve_strings(quotes))

import sys

sys.path.insert(0, './modules')
import module

for p in sys.path:
    print(p)

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]

print(module.prodl(ones))
print(module.suml(zeroes))