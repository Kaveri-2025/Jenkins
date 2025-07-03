import sys

def check_number(value):
    try:
        number = float(value)
        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        check_number(sys.argv[1])
    else:
        print("Usage: python check_number.py <number>")
