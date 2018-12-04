### PART ONE ###
# open file and read inputs
f = open('input.txt', "r")
inputs = f.readlines()
f.close()

# set starting frequency to 0
current_frequency = 0

# iterate through inputs, adding each to current frequency
for line in inputs:
	current_frequency += int(line)

# print result
print("Ending Frequency: " + str(current_frequency))

### PART TWO ###
# initialize dictionary of frequencies 
frequencies = {}

# set current_frequency to 0
current_frequency = 0

# iterate through inputs until finding a repeat frequency
current_index = 0
length = len(inputs)
while True:
	current_frequency += int(inputs[current_index % length])
	if str(current_frequency) in frequencies.keys():
		print("First Repeat: " + str(current_frequency))
		break
	else:
		frequencies[str(current_frequency)] = 1
		current_index  += 1