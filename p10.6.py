def calculate_name_value(name):
    # Convert the name to lowercase for case-insensitive calculation
    name = name.lower()

    # ASCII value of 'a' is 97, so subtracting 96 gives the alphabetical position
    name_value = sum(ord(char) - 96 for char in name if char.isalpha())

    return name_value

# Example usage:
name = input("Enter a name: ")
numeric_value = calculate_name_value(name)

print(f"The numeric value of the name {name} is: {numeric_value}")
