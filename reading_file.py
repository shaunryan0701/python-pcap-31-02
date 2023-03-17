
def count_word(word):
  try:
      words = []
      file = open('second_text_file.txt')
      for line in file:
          words += line.replace('.', ' ').replace(',', ' ').lower().split()
      print(words)
  except Exception as e:
      print("An error occurred: ", e)    

  return words.count(word)

word = 'of'
print('Ocurrence of', word, count_word(word))