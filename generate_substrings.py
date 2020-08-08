# Generate all substrings of length k and with alphabet
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
        smaller = generate_all_substrings(k - 1, list(set(alphabet) - set([c])))
        for s in smaller:
           if len(s) == k - 1:
               res.append(s + [c])
    # return sorted([v for v in res if len(v) == k])
    return res

def combine_all_generated_substrings(k, alphabet): 
    res = []
    for x in _generate_all_substrings(k, alphabet):
        res.append(''.join(x))

print(res)
print(len(res))
