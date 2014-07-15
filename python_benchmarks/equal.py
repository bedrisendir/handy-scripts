import sys
if __name__ == '__main__':
	print 'Please use main.py to run benchmarks'
	sys.exit(1)

def main(input_file, output_file):
	for line in input_file:
		output_file.write(line)
