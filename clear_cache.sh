#!/bin/bash                                                                                                                     

tmp_file="/var/work/bsendir1/cache.cleaner"

dd if=/dev/zero of="$tmp_file" bs=$((1024 * 1024 * 1024)) count=8 && rm "$tmp_file"
