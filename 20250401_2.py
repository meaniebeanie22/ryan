import string
from collections import defaultdict

frequency = defaultdict(int)
sentence = input().lower().split()

sentence = [x.strip(string.punctuation) for x in sentence]

for word in sentence:
    frequency[word] += 1

for word, number in frequency.items():
    print(f"{word}:{number}")
