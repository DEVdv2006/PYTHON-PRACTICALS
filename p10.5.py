def convert_rgb_to_base10(rgb_code):
    # Validate input length
    if len(rgb_code) != 6:
        raise ValueError("Invalid RGB color code. It should be a six-digit code.")

    # Convert hexadecimal to base 10
    red = int(rgb_code[0:2], 16)
    green = int(rgb_code[2:4], 16)
    blue = int(rgb_code[4:6], 16)

    return red, green, blue

# Example usage:
try:
    rgb_code = input("Enter a six-digit RGB color code: ")
    red, green, blue = convert_rgb_to_base10(rgb_code)

    print(f"Red: {red}, Green: {green}, Blue: {blue}")
except ValueError as e:
    print(e)
