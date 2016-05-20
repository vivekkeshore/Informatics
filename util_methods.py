__author__ = 'vkishore'

import itertools

bases = ['A', 'C', 'G', 'T']
bases_dict = {
  'A': 0,
  'C': 1,
  'G': 2,
  'T': 3,
  '0': 'A',
  '1': 'C',
  '2': 'G',
  '3': 'T'
}

# Approach O(n^k), k is len(pattern)
# kmers = [''.join(p) for p in itertools.product(bases, repeat=k)]

# Another approach O(k)
def pattern_to_number(pattern):
  pattern = pattern[::-1]
  index = 0
  for i in range(len(pattern)):
    index += bases_dict.get(pattern[i]) * (4 ** i)
  return index

def pattern_to_number_optimized(pattern):
  if not pattern:
    return

  last_char = pattern[-1:]
  prefix = pattern[:-1]

  return 4 * pattern_to_number(prefix) + bases_dict[last_char]


def number_to_pattern(index, k):
  pattern = ''
  while index > 0:
    pattern += str(index % 4)
    index //= 4
  pattern = pattern[::-1]
  pattern = ((k - len(pattern)) * '0') + pattern
  pattern = list(map(lambda char: bases_dict.get(char), pattern))

  return ''.join(pattern)

# def number_to_pattern_optimized(index, k):
#   if k == 1:
#     return bases_dict.get(str(k))
#
#   prefix_index = index // 4
#   rem = index % 4
#   char = bases_dict.get(str(rem))
#   prefix_pattern = number_to_pattern(prefix_index, k-1)
#
#   return prefix_pattern + char

def computing_frequencies(text, k):
  freq_array = [0 for _ in range(4 ** k)]

  for i in range(len(text) - k + 1):
    pattern = text[i: i+k]
    j = pattern_to_number_optimized(pattern)
    freq_array[j] += 1

  return freq_array

def clump_finding(genome, k, t, window_len):
  freq_patterns = set()
  clump = [0 for _ in range(4 ** k)]

  text = genome[0: window_len]
  freq_array = computing_frequencies(text, k)

  for i in range(4 ** k):
    if freq_array[i] >= t:
      clump[i] = 1

  for i in range(1, len(genome) - window_len + 1):
    first_pattern = genome[i-1: i-1+k]
    index = pattern_to_number_optimized(first_pattern)
    freq_array[index] -= 1
    last_pattern = genome[i + window_len - k: (i + window_len - k)+k]
    index = pattern_to_number_optimized(last_pattern)
    freq_array[index] += 1

    if freq_array[index] >= t:
      clump[index] = 1

  for i in range(4 ** k):
    if clump[i] == 1:
      pattern = number_to_pattern(i, k)
      freq_patterns.add(pattern)

  return freq_patterns


def freq_words_by_sorting(text, k):
  freq_patterns = set()
  index = []
  count = []

  for i in range(len(text) - k + 1):
    pattern = text[i: i+k]
    ind = pattern_to_number_optimized(pattern)
    index.append(ind)
    count.append(1)

  index.sort()
  for i in range(1, len(text) - k + 1):
    if index[i] == index[i-1]:
      count[i] = count[i-1] + 1

  max_count = max(count)
  for i in range(len(text) - k + 1):
    if count[i] == max_count:
      pattern = number_to_pattern(index[i], k)
      freq_patterns.add(pattern)

  return freq_patterns



import sys

data = sys.stdin.read().splitlines()
# k = sys.stdin.readline().splitlines()
# k = int(k[0])
# output = computing_frequencies(genome[0], k)
# for o in output:
#   sys.stdout.write(str(o) + ' ')
index, k = int(data[0]), int(data[1])
print(number_to_pattern(index, k))
