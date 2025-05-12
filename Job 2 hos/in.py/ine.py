import itertools
from nltk.corpus import words
import nltk

# Download word list (only needed once)
nltk.download('words')
english_words = set(words.words())

def find_word_combinations(letters):
    results = set()
    letters = letters.lower()

    # Try all lengths of words from 2 to the full length
    for i in range(2, len(letters)+1):
        for combo in itertools.permutations(letters, i):
            word = ''.join(combo)
            if word in english_words:
                results.add(word)
    return sorted(results)

# Example usage
user_input = input("Enter letters to find possible English words: ")
words_found = find_word_combinations(user_input)

print("\nPossible English words from your letters:")
for word in words_found:
    print(word)
