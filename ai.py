
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
  print('words in guess list ' + str(len(guess_list)))
  if len(data) == 0:
    #crane has been mathematically determined to be the most efficient starting word in wordle
    guess_word = 'crane'
  # elif len(data) == 1:
  #   #word with 5 remaining letters in top 10 most common letters. Might include using if word bank is larger. With smaller word banks it just reduces efficiency
  #   guess_word = 'toils'
  # tried_list.append(guess_word)
  # elif len(data) > 1:
  #   guess_word = choice(guess_list)
                  
  for guess in data:
    tried_list.append(guess['word'])

  # # redundant
  # for guess in tried_list:
  #   if guess in guess_list:
  #     guess_list.remove(guess)

  if len(data) < 1:
    return guess_word
  else:
    for word in data:
      print (word['word'])
      print (word['status'])
      word_parse = list(word['word'])
      status_parse = list(word['status'])
      i = 0
      while i < len(word_parse):
        letter = word_parse[i]
        # letter_index = word_parse.index(letter, word_parse.index(letter))
        letter_status = status_parse[i]
        # print(str(letter) + '=' + str(letter_status))
        if int(letter_status) == 0:
          print('words with ' + letter +' removed')
          for word in reversed(guess_list):
            if letter in list(word):
              guess_list.remove(word)
              # print(guess_list)
            # print(str(list(word)))
        elif int(letter_status) == 1:
          print('words without ' + letter + ' or has a ' + letter + ' in position ' + str(i+1) + ' removed')
          for word in reversed(guess_list):
            # print(word)
            # print(list(word)[letter_index])
            if (letter in list(word)[i]) or (letter not in list(word)):
              guess_list.remove(word)
        elif int(letter_status) == 2:
          print('Words without a ' + letter + ' in position ' + str(i+1) + ' removed')
          for word in reversed(guess_list):
            if letter not in list(word)[i]:
              guess_list.remove(word)
        i += 1
        
  temp_list = []
  for word in guess_list:
    word_parse =list(word)
    for letter in word_parse:
      temp_list.append(letter)
  print(temp_list)
  guess_word = choice(guess_list)

  print('********************')
  print('tried list:' + str(tried_list))

  if len(guess_list) < 20:
    print('**************')
    print('words remaining: ' + str(guess_list))
    print('**************')
    
  return guess_word