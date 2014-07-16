#!/usr/bin/env python
import getopt, json, sys

def decode_hex(string):
    ret = ''
    for index in range(len(string)/2):
        temp = string[index * 2] + string[index * 2 + 1]
        ret += chr(int(temp, 16))

    return ret

def encode_hex(string):
    ret = ''
    for char in string:
        ret += hex(ord(char))[2:]

    return ret

def grab_columns(input_file, output_file, encoder, columns):

    for line in input_file:
        line = line.strip()
        if line in '[]' or not line: continue

        if line.startswith(','):
            line = line[1:]
        if line.endswith(','):
            line = line[:-1]

        delim = ''
        record = json.loads(line)
        for col in record['columns']:
            if not columns or col[0] in columns:
                output_file.write(delim + encoder(col[1]))
                if delim == '': delim = ','
        output_file.write('\n')

if __name__ == '__main__':
    input_file = sys.stdin
    output_file = sys.stdout
    columns = []
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'i:o:c:', ['input=', 'output=', 'columns='])
    except getopt.GetoptError, ex:
        print ex.message
        sys.exit(1)

    for opt, val in opts:
        if opt in ('-i', '--input'):
            input_file = open(val)
        elif opt in ('-o', '--output'):
            output_file = open(val, 'w')
        elif opt in ('-c', '--columns'):
            columns = val.split(',')

    grab_columns(input_file, output_file, decode_hex, columns)
