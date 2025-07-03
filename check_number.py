def check_number(number):
    if number > 0:
        print("Success: The number is positive.")
    elif number < 0:
        print("Failure: The number is negative.")
    else:
        print("Failure: The number is zero.")

if __name__ == "__main__":
    # 🔽 Change this value to test different inputs
    input_value = 5
    
    check_number(input_value)
