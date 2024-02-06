def are_anagrams(word1, word2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_word1 = ''.join(word1.split()).lower()
    cleaned_word2 = ''.join(word2.split()).lower()

    # Check if the sorted characters of both words are the same
    return sorted(cleaned_word1) == sorted(cleaned_word2)

# Example usage:
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if are_anagrams(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")
