import sys, re

# Change to your character's name
listeners = ['Sen Isu']


# Skip the log info section
# And first channel change, since that is from the session start
START_LINE = 13
CHANNELS = ['local']
jumps = []
for file in sys.argv[1:]:
	with open(file, encoding="utf-16") as f:
		lines = f.readlines()

		channel = lines[6].strip().split('  ')[-1]
		listener = lines[8].strip().split('  ')[-1]

		if (channel in CHANNELS and listener in listeners):
			session = lines[9].strip().split()[-2:]

			# if session[0] in jumps:
			# 	jumps[session[0]].update({session[1]: []})
			# else:
			# 	jumps[session[0]] = {session[1]: []}

			for line in lines[START_LINE:]:
				if re.search('Channel changed to Local', line):
					results = re.search("\[ .* (.*) \].*Channel\ changed\ to\ Local\ :\ (.*)", line)
					jumps.append('{}\t{}\t{}'.format(session[0], results.group(1), results.group(2)))

					# jumps[session[0]][session[1]].append({results.group(1): results.group(2)})

print(jumps)
