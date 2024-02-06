def remove_whitespace_and_interleave(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.read().replace(" ", "")
            content2 = f2.read().replace(" ", "")

            # Interleave the characters of both strings
            interleaved_string = ''.join([char1 + char2 for char1, char2 in zip(content1, content2)])

            print("Interleaved String:", interleaved_string)
    except FileNotFoundError:
        print(f"Error: One or both files not found.")

# Example usage:
file1_name = input("Enter the first filename: ")
file2_name = input("Enter the second filename: ")

remove_whitespace_and_interleave(file1_name, file2_name)
