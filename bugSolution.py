def function_with_uncommon_error_fixed(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero!")  # Raise the exception
    return b / a

try:
    result = function_with_uncommon_error_fixed(0, 10)
    print(result)
except ZeroDivisionError as e:
    print("Error:", e)  # Handle the exception gracefully