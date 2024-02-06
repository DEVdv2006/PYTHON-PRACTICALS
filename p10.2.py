def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    result_tuple = (vowel_count, consonant_count)
    return result_tuple

# Example usage:
input_str = input("Enter a string: ")
result = count_vowels_and_consonants(input_str)

print("Number of vowels:", result[0])
print("Number of consonants:", result[1])
