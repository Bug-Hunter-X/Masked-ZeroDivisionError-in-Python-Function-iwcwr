def function_with_uncommon_error(a, b):
    if a == 0:
        return 0  # This is incorrect; should handle division by zero
    return b / a

result = function_with_uncommon_error(0, 10)
print(result)  # This will print 0, masking the actual error