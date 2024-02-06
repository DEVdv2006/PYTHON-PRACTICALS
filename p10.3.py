def format_date(input_date):
    # Split the input date into day, month, and year
    day, month, year = map(int, input_date.split('/'))

    # Format the date in MM-DD-YYYY
    formatted_date = f"{month:02d}-{day:02d}-{year}"

    return formatted_date

# Example usage:
input_date = input("Enter a date (DD/MM/YYYY): ")

try:
    formatted_date = format_date(input_date)
    print("Formatted date:", formatted_date)
except ValueError:
    print("Invalid date format. Please enter the date in DD/MM/YYYY format.")
