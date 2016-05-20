__author__ = 'vkishore'

import sys

lines = sys.stdin.read().splitlines()
pattern, text = lines[0], lines[1]

pattern_len = len(pattern)
text_len = len(text)

def pattern_count(text, pattern):
  positions = []
  for i in range((text_len - pattern_len) + 1):
    if text[i: i+pattern_len] == pattern:
      positions.append(i)
  return positions

positions = pattern_count(text, pattern)
for pos in positions:
  sys.stdout.write(str(pos) + ' ')
