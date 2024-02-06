import string

def calculate_average_lengths(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

            # Split the content into sentences
            sentences = content.split('.')

            # Remove punctuation and split into words
            words = [word.strip(string.punctuation) for sentence in sentences for word in sentence.split()]

            # Calculate average word length
            average_word_length = sum(len(word) for word in words) / len(words) if words else 0

            # Calculate average sentence length
            average_sentence_length = len(sentences) / len([word for word in words if word])

            return average_word_length, average_sentence_length
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

# Example usage:
file_name = input("Enter the filename: ")

result = calculate_average_lengths(file_name)

if result is not None:
    print(f"Average word length: {result[0]:.2f} characters")
    print(f"Average sentence length: {result[1]:.2f} sentences")
