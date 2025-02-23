#!/usr/bin/env python

import sys

current_word = None
current_count = 0

# Read each line from standard input
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t')

    # Convert count to integer
    try:
        count = int(count)
    except ValueError:
        continue
    
    # If the word is the same as the previous one, aggregate counts
    if current_word == word:
        current_count += count
    else:
        # If the word is different, print the previous word and its count
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# Print the last word and its count
if current_word == word:
    print(f"{current_word}\t{current_count}")
