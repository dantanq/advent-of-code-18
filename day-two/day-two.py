from collections import Counter

### PART ONE ###
# get inputs
f = open('input.txt', "r")
inputs = f.readlines()
f.close()

# counts of IDs with exactly two or three of any letter
two_count = 0
three_count = 0

# iterate through each input
for line in inputs:
	# find counts of each letter in input
	counts =  Counter(line)
	two = False
	three = False
	for count in counts.keys():
		if counts[count] == 2:
			two = True
		elif counts[count] == 3:
			three = True
		# don't need to keep checking if have found letters which occur exactly two and three times
		if two and three:
			break
	if two:
		two_count += 1
	if three:
		three_count += 1

# find and print checksum
checksum = two_count * three_count
print("checksum: " + str(checksum))

### PART TWO ###
# length of each ID
length = len(inputs[0])

# iterate through each letter in ID
for i in range(0, length):
	# remove char at index i from each ID
	# keep track of if we've seen each input before
	new_inputs = []
	found = False
	for line in inputs:
		new_string = line[0:i] + line[i+1:]
		if new_string in new_inputs:
			found = True
			print("common string: " + new_string)
			break
		else:
			new_inputs.append(new_string)
	if found:
		break
