def count_alphabet_occurrences(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()

            # Initialize a dictionary to store alphabet occurrences
            alphabet_occurrences = {}
            
            # Count occurrences of each alphabet
            for char in content:
                if char.isalpha():
                    alphabet_occurrences[char] = alphabet_occurrences.get(char, 0) + 1

            return alphabet_occurrences
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

# Example usage:
file_name = input("Enter the filename: ")

result = count_alphabet_occurrences(file_name)

if result is not None:
    print("Alphabet occurrences in the file:")
    for char, count in result.items():
        print(f"{char}: {count}")
