#python select_random_word.py
# !=yellow
# @=green
# #=grey
import random



def read_words():
	five_letter_words = []
	with open("popular_five_letter_words.txt","r") as f:
		words = f.readlines()
		f.close()
	for word in words:
		five_letter_words.append(word[:-1])
	return five_letter_words


def select_random_word(potential_words):
	duplicate_score = 5
	while duplicate_score != 0:
		word = random.choice(potential_words)
		duplicate_score = 0
		for i in range(5):
			for j in range(i+1,5):
				if word[i] == word[j]:
					duplicate_score = duplicate_score + 1
					break
	return word


def interpret(interpreted_word, word, discarded, confirmed, yellow):
	for i in range(len(word)):
		if interpreted_word[i] == '!':
			yellow[i] = word[i]
		if interpreted_word[i] == '@':
			confirmed[i] = word[i]
		if interpreted_word[i] == '#':
			if word[i] not in discarded:
				discarded.append(word[i])
	return [discarded,confirmed,yellow]


def make_new_word_list(old_doc_name, old_word_list, discarded, confirmed, yellow):
	new_word_list = []


	#discarded portion
	for potential_word in old_word_list:
		check = 0
		for one_letter in discarded:
			if one_letter in potential_word:
				check = 1
		if check == 0:
				new_word_list.append(potential_word)
	old_word_list =  new_word_list

	new_word_list = []
	#confirmed portion
	for potential_word in old_word_list:
		check = 0
		for i in confirmed.keys():
			if potential_word[i] != confirmed[i]:
				check = 1
				break
		if check == 0:
			if potential_word not in new_word_list:
				new_word_list.append(potential_word)
	

	old_word_list = new_word_list
	#yellow portion
	new_word_list = []
	for potential_word in old_word_list:
		check = 0
		for i in yellow.keys():
			if potential_word[i] == yellow[i] or yellow[i] not in potential_word:
				check = 1
		if check == 0:
			new_word_list.append(potential_word)

	#print(old_word_list)

	new_doc_name = old_doc_name[:-1] + str(int(old_doc_name[-1])+1)
	print(new_doc_name)

	with open(new_doc_name+'.txt','w') as f:
		for word in new_word_list:
			f.write(word)
			f.write('\n')
		f.close()
	print(new_word_list)
	return [new_doc_name,new_word_list]


def one_iteration(potential_words, doc_name, discarded, confirmed, yellow):
	guessed_word = select_random_word(potential_words)
	print(guessed_word)
	interpreted_word = input()

	results = interpret(interpreted_word, guessed_word, discarded, confirmed, yellow)
	discarded = results[0]
	confirmed = results[1]
	yellow = results[2]

	print(discarded,confirmed,yellow)
	results2 = make_new_word_list(doc_name, potential_words, discarded, confirmed, yellow)
	doc_name = results2[0]
	potential_words = results2[1]

	print('Enter 0 to print new list, otherwise 1')
	choice = input()
	if choice == '0':
		print(potential_words)

	return [potential_words, doc_name, discarded, confirmed, yellow]





############################################################################
####   main   ###########
potential_words = read_words()
discarded = []
confirmed = {}
yellow = {}
doc_name = 'potential_words_1'



# guessed_word = select_random_word(potential_words)
# print(guessed_word)
# interpreted_word = input()

# results = interpret(interpreted_word, guessed_word, discarded, confirmed, yellow)
# discarded = results[0]
# confirmed = results[1]
# yellow = results[2]

# print(discarded,confirmed,yellow)
# results2 = make_new_word_list(doc_name, potential_words, discarded, confirmed, yellow)
# doc_name = results2[0]
# potential_words = results2[1]

# print('Enter 0 to print new list, otherwise 1')
# choice = input()
# if choice == '0':
# 	print(potential_words)
# print(potential_words)






for i in range(6):
	results3 = one_iteration(potential_words, doc_name, discarded, confirmed, yellow)
	potential_words = results3[0]
	doc_name = results3[1]
	discarded = results3[2]
	confirmed = results3[3]
	yellow = results3[4]


##############################################################################

# potential_words = read_words()

# print(select_random_word(potential_words))

# discarded = []
# confirmed = {}
# yellow = {}
# doc_name = 'potential_words_1'


# #correct_word = 'abbey'

# interpreted_word = '!###!'
# guessed_word = 'yzzza'

# results = interpret(interpreted_word, guessed_word,discarded,confirmed,yellow)

# discarded = results[0]
# confirmed = results[1]
# yellow = results[2]

# print(discarded,confirmed,yellow)
# results2 = make_new_word_list(doc_name, potential_words, discarded, confirmed, yellow)
# doc_name = results[2]
# potential_words = results[1]