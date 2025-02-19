def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty or all non-numeric list
    return sum(numeric_numbers) / len(numeric_numbers) 
    