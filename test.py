data = [{'word': 'crane', 'status': '01102'} , {'word': 'enemy', 'status': '11112'}]

print(data[0]['word'])
letter_index = list(data[1]['word']).index('e', 0)
print(letter_index)