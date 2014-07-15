import sys
if __name__ == '__main__':
	print 'Please use main.py to run benchmarks'
	sys.exit(1)

def main(a,b):
	i=0
	while True:
    		string=raw_input()
		i+=1
		if i == 10: i = 0
                if i == 0:
		    print string
    		    sys.stdout.flush()
		else:
		    print None
		    sys.stdout.flush()
