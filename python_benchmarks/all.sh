#!/bin/bash
function bm {
	echo ">>> Timing $2 with dataset $1"
	time main.py -i "$1".txt -o "$2".out -b "$2"
	echo
}

bm "$1" read
bm "$1" equal
bm "$1" write
bm "$1" cpu
bm "$1" mem
