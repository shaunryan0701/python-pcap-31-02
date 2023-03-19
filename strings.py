sample_story = '''Once I'm awaken, I'll sacrifice your soul to the ruler of darkness.'''

def get_logest_word(story):
    words = story.replace('.', '').replace(',', '').split()
    print(words)
    max_len_word = ''
    for word in words:
        if len(word) > len(max_len_word):
            max_len_word = word
    return max_len_word       

print(get_logest_word(sample_story))