__author__ = 'vkishore'
import sys

lines = sys.stdin.read().splitlines()
text, kmer = lines[0], int(lines[1])
# text = 'CGGAAGCGAGATTCGCGTGGCGTGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGGCGTGATTCGAGCGGCGGATTCGAGATTCCGGGCGTGCGGGCGTGAAGCGCGTGGAGGAGGCGTGGCGTGCGGGAGGAGAAGCGAGAAGCCGGATTCAAGCAAGCATTCCGGCGGGAGATTCGCGTGGAGGCGTGGAGGCGTGGAGGCGTGCGGCGGGAGATTCAAGCCGGATTCGCGTGGAGAAGCGAGAAGCGCGTGCGGAAGCGAGGAGGAGAAGCATTCGCGTGATTCCGGGAGATTCAAGCATTCGCGTGCGGCGGGAGATTCAAGCGAGGAGGCGTGAAGCAAGCAAGCAAGCGCGTGGCGTGCGGCGGGAGAAGCAAGCGCGTGATTCGAGCGGGCGTGCGGAAGCGAGCGG'
# kmer = 12
text_len = len(text)

def pattern_count(text, pattern):
  c = 0
  for i in range((text_len - kmer) + 1):
    if text[i: i+kmer] == pattern:
      c += 1
  return c

pattern_dict = {}
max_count = 0
for i in range((text_len - kmer) + 1):
  pattern = text[i: i+kmer]
  count = pattern_count(text, pattern)
  try:
    patterns = pattern_dict[count]
    patterns.append(pattern)
  except KeyError:
    patterns = [pattern]

  pattern_dict[count] = patterns
  if count > max_count:
    max_count = count

patterns = set(pattern_dict.get(max_count))
for pattern in patterns:
  print(pattern),
