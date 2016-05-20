__author__ = 'vkishore'

import sys # you must import "sys" to read from STDIN

lines = sys.stdin.read().splitlines()  # read in the input from STDIN
text, pattern = lines[0], lines[1]

pattern_len = len(pattern)
text_len = len(text)

c = 0
for i in range((text_len - pattern_len) + 1):
  if text[i: i+pattern_len] == pattern:
    c += 1
print(c)