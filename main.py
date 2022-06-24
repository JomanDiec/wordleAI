import importlib.util as ilu

print_all = True


def preloader():
  global print_all
  spec = ilu.spec_from_file_location('ai', 'ai.py')  
  module = ilu.module_from_spec(spec)
  spec.loader.exec_module(module)
  print_all = module.print_all
  
def strategy_test(data, word_bank):
  spec = ilu.spec_from_file_location('ai', 'ai.py')  
  module = ilu.module_from_spec(spec)
  spec.loader.exec_module(module)
  ai_word = module.run(data, word_bank)
  return ai_word.lower()
  
def status_calc(word, word_test):
  output = ""
  for i, letter in enumerate(word_test):
    if letter == word[i]:
      output += "2"
    elif letter in word:
      output += "1"
    else:
      output += "0"
  return output
  
def wordle():
  word_bank = [
    'south',
    'drama',
    'built',
    'tough',
    'agree',
    'cover',
    'taste',
    'other',
    'badly',
    'forum',
    'score',
    'leave',
    'fixed',
    'steel',
    'shell',
    'enter',
    'smith',
    'tower',
    'gross',
    'jimmy',
    'heart',
    'delay',
    'since',
    'metal',
    'newly',
    'ready',
    'tight',
    'guess',
    'front',
    'quick',
    'board',
    'mouse',
    'photo',
    'begun',
    'fluid',
    'horse',
    'small',
    'trend',
    'rough',
    'route',
    'fleet',
    'bases',
    'sheet',
    'stick',
    'tired',
    'motor',
    'bench',
    'times',
    'quiet',
    'buyer',
    'happy',
    'magic',
    'doing',
    'movie',
    'chain',
    'apart',
    'those',
    'woman',
    'three',
    'ought',
    'style',
    'enemy',
    'undue',
    'plate',
    'admit',
    'stock',
    'brown',
    'japan',
    'angry',
    'model',
    'track',
    'noted',
    'alive',
    'phase',
    'short',
    'above',
    'glass',
    'shall',
    'flash',
    'baker',
    'dream',
    'dress',
    'break',
    'spoke',
    'serve',
    'world',
    'scale',
    'might',
    'march',
    'sugar',
    'trial',
    'robin',
    'usual',
    'money',
    'along',
    'local',
    'thick',
    'beach',
    'crowd',
    'trust',
  ]
  total_points = 0
  possible_points = len(word_bank) * 6
  solved_qty = 0
 
  for word in word_bank:
    # print(print_all)
    if print_all:
      print("")
      print("----- Correct Word: ", word, "-----")
    word_status = 1
    round_points = 6
    game_round = 1
    data = []
    while word_status == 1 and game_round <= 6:
      word_test = strategy_test(data, word_bank)
      if print_all:
        print("AI Word: ", word_test)
      if word_test == word:
        if print_all:
          print("Correct! Round Points: ", round_points )
        total_points += round_points
        word_status = 0
        solved_qty += 1
      else:
        status = status_calc(word, word_test)
        data.append({'word':word_test, 'status':status})
        round_points -= 1
      game_round+=1
      if game_round == 7:
        if print_all:
          print("No points")
  point_plural = "s"
  if total_points == 1:
    point_plural = ""
  word_plural = "s"
  if solved_qty == 1:
    word_plural = ""  

  if print_all:
    print("")
    print("")
  print("========*** RESULTS ***========")
  print(f"{total_points} point{point_plural} out of {possible_points} possible points ({round(total_points/possible_points, 3)*100}%)")
  print(f"{solved_qty} word{word_plural} solved out of {len(word_bank)} words ({round(solved_qty/len(word_bank), 3)*100}%)")

preloader()  
wordle()
