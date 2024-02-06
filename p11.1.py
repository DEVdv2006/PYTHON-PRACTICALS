def create_and_write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File '{file_path}' created and written successfully.")

def read_entire_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    print(f"Content of '{file_path}':\n{content}")

def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        print(f"Reading '{file_path}' line by line:")
        for line in file:
            print(line.strip())

def write_string_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"String written to '{file_path}' successfully.")

def write_list_to_file(file_path, lines):
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')
    print(f"List of strings written to '{file_path}' successfully.")

def count_lines_and_words(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)

    print(f"Number of lines in '{file_path}': {line_count}")
    print(f"Number of words in '{file_path}': {word_count}")

# Example usage:
file_path = "sample_file.txt"
string_to_write = "Hello, this is a sample string to write to a file."

# Create and write to a file
create_and_write_file(file_path, string_to_write)

# Read entire file
read_entire_file(file_path)

# Read file line by line
read_file_line_by_line(file_path)

# Write a string to a file
write_string_to_file(file_path, "This is a new string written to the file.")

# Write a list of strings to a file
lines_to_write = ["Line 1", "Line 2", "Line 3"]
write_list_to_file(file_path, lines_to_write)

# Count lines and words in a file
count_lines_and_words(file_path)
