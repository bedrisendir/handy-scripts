import sys
if __name__ == '__main__':
	print 'Please use main.py to run benchmarks'
	sys.exit(1)

datasets = {
	'1k':   10 ** 3,
	'10k':  10 ** 4,
	'100k': 10 ** 5,
	'1m':   10 ** 6,
	'10m':  10 ** 7,
	#'100m': 10 ** 8,
	#'1b':   10 ** 9,
}

def main(*args):
	for name in datasets:
		print 'Writing dataset ' + name
		f = open(name + '.txt', 'w')
		for i in range(datasets[name]):
			f.write('.' * 100 + '\n')
		f.close()
