def display_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

            # Extract and display all numbers using isdigit()
            numbers = [word for word in content.split() if word.isdigit()]
            
            if numbers:
                print(f"Numbers found in the file '{filename}':")
                for number in numbers:
                    print(number)
            else:
                print(f"No numbers found in the file '{filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Example usage:
file_name = input("Enter the filename: ")

display_numbers_from_file(file_name)
