import json, sys
if __name__ == '__main__':
	print 'Please use main.py to run benchmarks'
	sys.exit(1)

def main(input_file, output_file):
	for line in input_file:
		#output_file.write(line.strip()*10 + '\n')
		 output_file.write(''.join([line.strip() for num in range(10)]) +'\n')
