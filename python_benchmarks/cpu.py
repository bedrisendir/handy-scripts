import sys
if __name__ == '__main__':
	print 'Please use main.py to run benchmarks'
	sys.exit(1)

def main(input_file, output_file):
	i = 0
	for line in input_file:
		temp = ''
		for char in line:
			temp += char

		i += 1
		if i == 10000: i = 0
		if i == 0:
			output_file.write(line)
