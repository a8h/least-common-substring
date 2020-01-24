# Try to find the least common substring

import collections
import heapq

substring_counts = collections.defaultdict(int)

def count_substrings_in_word(k, word):
   for i in range(len(word) - k + 1):
       substring_counts[word[i:i+k]] += 1


def count_words():
    with open('words_alpha.txt') as f:
        for word in set(f.read().split()):
           count_substrings_in_word(2, word)

# Get n rarest substrings from a dictionary
def get_n_rarest(d):
    return heapq.nsmallest(d, substring_counts.items(), key = lambda x: x[1])

def get_n_most_common(d):
    return heapq.nlargest(d, substring_counts.items(), key = lambda x: x[1])

def get_substring_count(substring):
    return substring_counts[substring]

# k is the size of heap to look in
# Not guaranteed to find anything
def rarest_substrings_with_specific_alphabet(k, alphabet):
    substrings_found = []
    for s, sc in get_n_rarest(k):
        found = True
        for c in s:
            if c not in alphabet:
               found = False
        if found:
           substrings_found.append((s, sc))
    return substrings_found


# Generate all substrings of length k and with alphabet
# Could use library, but implemented by hand
def _generate_all_substrings(k, alphabet):
    #Case analysis
    #For the n-th character: 
    # 1. generate all the substrings of size k-1 with the alphabet excluding the n-th character and then insert the n-th character
    # 2. generate all the substrings of size k with the alphabet excluding the n-th character
    res = []
    smaller = []
    if k == 0 or len(alphabet) == 0:
        return [[]]
    for c in alphabet:
        smaller = _generate_all_substrings(k - 1, list(set(alphabet) - set([c])))
        for s in smaller:
           if len(s) == k - 1:
               res.append(s + [c])
    return res

def combine_all_generated_substrings(k, alphabet): 
    res = []
    for x in _generate_all_substrings(k, alphabet):
        res.append(''.join(x))
    return res

def find_missing_generated_substrings(k, alphabet):
    # Ignore the semi-colon (';') character
    gen = combine_all_generated_substrings(2, 'asdfjkl')
    res = []
    for x in gen:
        res.append((x, substring_counts[x]))
    return sorted(res, key = lambda x: x[1])

count_words()
print(get_n_rarest(20))
print(get_n_most_common(20))
print(rarest_substrings_with_specific_alphabet(200, 'asdfjkl'))
print(find_missing_generated_substrings(2, 'asdfjkl'))
print(get_substring_count('jf'))
