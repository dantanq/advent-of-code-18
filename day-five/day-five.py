import string

### PART ONE ###
# get input
f = open('input.txt', 'r')
polymer = f.readline().strip()
f.close()

# map lower and uppercase letters to each other
lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase
upper = {}
lower = {}
for i in range(0, 26):
	upper[upper_alphabet[i]] = lower_alphabet[i]
	lower[lower_alphabet[i]] = upper_alphabet[i]

print("initial length of polymer: " + str(len(polymer)))

# go through polymer, destroying elements as we go
def reaction(polymer):
	current_index = 0
	while current_index < len(polymer)-1:
		check = polymer[current_index]
		if check in lower_alphabet:
			opposite = lower[check]
		else:
			opposite = upper[check]
		if polymer[current_index+1] == opposite:
			polymer = polymer[0:current_index] + polymer[current_index+2:]
			current_index -= 1
		else:
			current_index += 1
	return polymer

# print length of polymer
new_polymer = reaction(polymer)
print("final length of polymer: " + str(len(new_polymer)))

### PART TWO ###
# iterate through every letter, checking the length of the reacted polymer
min_length = len(new_polymer)
char_check = "a"
for letter in lower_alphabet:
	check = new_polymer.replace(letter, "")
	check = check.replace(lower[letter], "")
	check = reaction(check)
	if len(check) < min_length:
		min_length = len(check)
		char_check = letter
print("removing " + char_check + "/" + lower[char_check] + " results in a polymer of length: " + str(min_length))