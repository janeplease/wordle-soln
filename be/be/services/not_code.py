from english_words import english_words_lower_alpha_set

popular_all_words = list(english_words_lower_alpha_set)

popular_five_letter_words = []

for word in popular_all_words:
	if len(word) == 5:
		popular_five_letter_words.append(word)

popular_five_letter_words.sort()

with open("popular_five_letter_words.txt","w") as f:
	for word in popular_five_letter_words:
		f.write(word)
		f.write('\n')


