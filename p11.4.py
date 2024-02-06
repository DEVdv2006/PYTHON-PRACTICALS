import re

def censor_four_letter_words(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

            # Use regular expression to find and censor four-letter words
            censored_content = re.sub(r'\b\w{4}\b', '****', content)

            with open(output_filename, 'w') as output_file:
                output_file.write(censored_content)

        print(f"Censoring complete. Result saved in '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")

# Example usage:
input_file_name = input("Enter the input filename: ")
output_file_name = input("Enter the output filename: ")

censor_four_letter_words(input_file_name, output_file_name)
