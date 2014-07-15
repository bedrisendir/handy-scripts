#!/usr/bin/env python
import getopt, sys

benchmarks = ['read', 'equal', 'write', 'cpu', 'mem', 'generate']

def main(args):
	input_file = sys.stdin
	output_file = sys.stdout
	benchmark = None

	try:
		opts, args = getopt.getopt(args, 'i:o:b:')
	except getopt.GetoptError, ex:
		print ex.message
		sys.exit(1)

	for opt, val in opts:
		if opt == '-i':
			input_file = open(val)
		elif opt == '-o':
			output_file = open(val, 'w')
		elif opt == '-b' and val in benchmarks:
			benchmark = val

	if not benchmark:
		print 'Please specify a valid benchmark with -b: {}'.format(benchmarks)

	if benchmark == 'read':
		import read as bench
	elif benchmark == 'equal':
		import equal as bench
	elif benchmark == 'write':
		import write as bench
	elif benchmark == 'cpu':
		import cpu as bench
	elif benchmark == 'mem':
		import mem as bench
	elif benchmark == 'generate':
		import generate as bench

	bench.main(input_file, output_file)

if __name__ == '__main__':
	main(sys.argv[1:])
