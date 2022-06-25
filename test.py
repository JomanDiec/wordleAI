data = [{'word': 'crane', 'status': '01102'} , {'word': 'enemy', 'status': '11112'}]

print(data[0]['word'])
letter_index = list(data[1]['word'])[0+1]
print(letter_index)

letters = ['R', 'E', 'T', 'O', 'P', 'A']
words_list = ["TOP", "CUT", "REPORT", "GOOD"]

final_list = [word for word in words_list if set(word).issubset(set(letters))]
print(final_list)