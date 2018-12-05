### PART ONE ###
# get input
f = open('input.txt', 'r')
input = f.readlines()
f.close()

# keep dictionary mapping position to number of claims
num_claims = {}

# for part two - list of IDs which, at time of first iteration, have no overlap
no_overlap = []

# iterate over lines in input
for line in input:
	# split line
	ID, at, placement, dimensions = line.split()
	# get x and y coordinates of cut
	x, y = placement.split(',')
	# remove ":" from y coordinate
	y = y[:len(y)-1]
	# get dimensions of cut
	x_dim, y_dim = dimensions.split('x')
	# convert strints to int
	x, y = int(x), int(y)
	x_dim, y_dim = int(x_dim), int(y_dim)
	# increment number of claims for each coordinate in claim by 1
	overlap = False
	for x_coordinate in range(x+1, x+x_dim+1):
		for y_coordinate in range(y+1, y+y_dim+1):
			coordinates = str(x_coordinate) + "," + str(y_coordinate)
			if coordinates in num_claims.keys():
				num_claims[coordinates] += 1
				overlap = True
			else:
				num_claims[coordinates] = 1
	# for part two - if doesn't overlap, add to no_overlap
	if not overlap:
		no_overlap.append(int(ID[1:]))

# count and print coordinates with >1 number of claims
count = 0
for coordinate in num_claims.keys():
	if num_claims[coordinate] > 1:
		count += 1
print("overlapping square inches: " + str(count))

### PART TWO ###
for line in no_overlap:
	# get line with matching ID
	check = input[line - 1]
	# split line
	ID, at, placement, dimensions = check.split()
	# get x and y coordinates of cut
	x, y = placement.split(',')
	# remove ":" from y coordinate
	y = y[:len(y)-1]
	# get dimensions of cut
	x_dim, y_dim = dimensions.split('x')
	# convert strints to int
	x, y = int(x), int(y)
	x_dim, y_dim = int(x_dim), int(y_dim)
	# check if coordinates have any overlap
	overlap = False
	for x_coordinate in range(x+1, x+x_dim+1):
		for y_coordinate in range(y+1, y+y_dim+1):
			coordinates = str(x_coordinate) + "," + str(y_coordinate)
			if num_claims[coordinates] > 1:
				overlap = True
				break
	if not overlap:
		print("ID of claim with no overlap: " + ID)
		break

