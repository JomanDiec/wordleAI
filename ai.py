
# STATUS CODES
# 2 - (Green) correct letter in correct place
# 1 - (Yellow) letter in word but wrong place
# 0 - (Gray) letter not in word

# EXAMPLE: 
# If the answer is “COAST” but you guessed “DETER” and “BRAIN”, your argument will look like this.:

# data = [
#   {“word”: “deter”, “status”: “00100”}
#   {“word”:”brain”,”status”:”00200”}
# ]


# Set print_all to True if you want to see all messages
print_all = True
from random import*
import copy
tried_list = []

def run(data, word_list):
  guess_word = ''
  guess_list = copy.deepcopy(word_list)
  print(data)
  if len(data) == 0:
    guess_word = 'crane'
  # elif len(data) == 1:
  #   guess_word = 'toils'
  # tried_list.append(guess_word)
  elif len(data) > 1:
    guess_word = choice(guess_list)
                  
  for guess in data:
    tried_list.append(guess['word'])

  for guess in tried_list:
    if guess in guess_list:
      guess_list.remove(guess)

  if len(data) < 1:
    return guess_word
  else:
    for word in data:
      print (word['word'])
      print (word['status'])
      word_parse = list(word['word'])
      status_parse = list(word['status'])
      for letter in word_parse:
        if word_parse.count(letter) < 2:
          letter_index = word_parse.index(letter, word_parse.index(letter))
        else:
          letter_index = word_parse.index(letter, word_parse.index(letter)+1)
        letter_status = status_parse[letter_index]
        # print(str(letter) + '=' + str(letter_status))
        if int(letter_status) == 0:
          print('words with ' + letter +' removed')
          for word in reversed(guess_list):
            if letter in list(word):
              guess_list.remove(word)
              # print(guess_list)
            # print(str(list(word)))
        elif int(letter_status) == 1:
          print('words without ' + letter + ' or has a ' + letter + ' in position ' + str(letter_index+1) + ' removed')
          for word in reversed(guess_list):
            # print(word)
            # print(list(word)[letter_index])
            if (letter in list(word)[letter_index]) or (letter not in list(word)):
              guess_list.remove(word)
        elif int(letter_status) == 2:
          print('Words without a ' + letter + ' in position ' + str(letter_index+1) + ' removed')
          for word in reversed(guess_list):
            if letter not in list(word)[letter_index]:
              guess_list.remove(word)

  guess_word = choice(guess_list)
  
  if len(guess_list) < 50:
    print('**************')
    print('word remaining: ' + str(guess_list))
    
  print('********************')
  # print(rand_word)
  # print('guess list:' + str(guess_list))
  print('tried list:' + str(tried_list))
  return guess_word