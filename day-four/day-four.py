from collections import Counter

### PART ONE ###
f = open('input.txt', 'r')
inputs = f.readlines()
f.close()

# sort inputs by time
inputs = sorted(inputs)

# keep track of guard numbers, etc.
guard_number = "#0"
guard_times = {}
last_fall = 0
last_wake = 0

# iterate over each line in input
for line in inputs:
	time = line[12:17]
	action = line[19:].split()
	# guard clocking in
	if action[0] == "Guard":
		guard_number = action[1]
		if guard_number not in guard_times.keys():
			guard_times[guard_number] = []
	# guard falls asleep
	elif action[0] == "falls":
		last_fall = int(time[3:])
	# guard wakes up
	else:
		last_wake = int(time[3:])
		guard_times[guard_number] += [x for x in range(last_fall, last_wake)]

# find guard who is asleep longest by finding guard with longest length in guard_times
maximum = 0
sleepiest_guard = "#0"
for guard in guard_times.keys():
	if len(guard_times[guard]) > maximum:
		maximum = len(guard_times[guard])
		sleepiest_guard = guard
# find when guard is most likely to be asleep
sleepy_times = Counter(guard_times[sleepiest_guard])
sleepiest_time = 0
maximum = 0
for minute in sleepy_times.keys():
	if sleepy_times[minute] > maximum:
		maximum = sleepy_times[minute]
		sleepiest_time = minute
print("the sleepiest guard is " + sleepiest_guard + " at " + str(sleepiest_time))

### PART TWO ###
maximum = 0
most_consistent_guard = "#0"
sleeps_at = 0
for guard in guard_times.keys():
	counts = Counter(guard_times[guard])
	for minute in counts.keys():
		if counts[minute] > maximum:
			maximum = counts[minute]
			most_consistent_guard = guard
			sleeps_at = minute
print (most_consistent_guard + " usually sleeps at " + str(sleeps_at))