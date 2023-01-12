with open("all_words.txt","r") as f:
	five_letter_words = []
	words = f.readlines()
	for word in words:
		if len(word) == 6:
			five_letter_words.append(word[:-1])
	f.close()


with open("five_letter_words.txt","w") as f:
	for i in five_letter_words:
		f.write(i)
		f.write('\n')
	f.close()