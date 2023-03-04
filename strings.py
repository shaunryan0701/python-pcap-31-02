sample_story = '''Once I'm awaken, I'll sacrifice your soul to the ruler of darkness.'''

def get_logest_word(story):
    words = story.replace('.', '').replace(',', '').split()
    print(words)
    max_length_word = ''
    for word in words:
        if len(word) > len(max_length_word):
            max_length_word = word
    return max_length_word       

print(get_logest_word(sample_story))