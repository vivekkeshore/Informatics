__author__ = 'vkishore'

import sys # you must import "sys" to read from STDIN

text = sys.stdin.read().splitlines()
text = text[0]
text_len = len(text)

DNA = {
  'A': 'T',
  'T': 'A',
  'G': 'C',
  'C': 'G'
}
reverse_complement = ''
for char in text:
  reverse_complement += DNA[char]

print(reverse_complement[::-1])
