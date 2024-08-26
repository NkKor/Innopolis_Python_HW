text = input()
letter_counter = {}
for letter in text.lower():
    if letter.isalpha():
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1
sorted_letters = sorted(letter_counter, key=letter_counter.get, reverse= True)
print("".join(sorted_letters[:5]))