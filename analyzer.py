import sys, re, json, argparse

# Change to your character's name
listeners = ['Sen Isu']


parser = argparse.ArgumentParser(description='Analyze EVE Online chat logs to determine jumps made', formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--output-format', dest='format', type=str, help='Output format\n\tsimple: tab-separated list of jumps\n\ttotals: total jumps per day\n\tdetailed: JSON with all info (including session changes)', choices=['simple', 'totals', 'detailed'], default='simple')
parser.add_argument('files', help='Chat logs to analyze', nargs='+')
args = parser.parse_args()
# Start at line 13 to skip the log info section
# And first channel change, since that is from the session start
START_LINE = 13
CHANNELS = ['local']
jumps = [] if args.format == 'simple' else {}
for file in args.files:
	with open(file, encoding="utf-16") as f:
		lines = f.readlines()

		channel = lines[6].strip().split('  ')[-1]
		listener = lines[8].strip().split('  ')[-1]

		if (channel in CHANNELS and listener in listeners):
			session = lines[9].strip().split()[-2:]

			# if session[0] in jumps:
			# 	if args.format == 'detailed':
			# 		jumps[session[0]].update({session[1]: []})
			# 	elif args.format == 'totals':
			# 		jumps[session[0]] += 1
			# else:
			# 	if args.format == 'detailed':
			# 		jumps[session[0]] = {session[1]: []}
			# 	elif args.format == 'totals':
			# 		jumps[session[0]] = 0

			for line in lines[START_LINE:]:
				if re.search('Channel changed to Local', line):
					results = re.search("\[ (.*) (.*) \].*Channel\ changed\ to\ Local\ :\ (.*)", line)

					if args.format == 'simple':
						jumps.append('{}\t{}\t{}'.format(results.group(1), results.group(2), results.group(3)))
					# elif args.format == 'detailed':
					# 	jumps[session[0]][session[1]].append({results.group(2): results.group(3)})
					elif args.format == 'totals':
						if results.group(1) in jumps:
							jumps[results.group(1)] += 1
						else:
							jumps[results.group(1)] = 0
if args.format == 'simple':
	for j in jumps:
		print(j)
elif args.format == 'detailed':
	print(json.dumps(jumps))
elif args.format == 'totals':
	for j, i in sorted(jumps.items()):
		print(j, i, sep='\t')
