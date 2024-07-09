"""
Raise consecutive natural numbers to chosen power and observe differences between results.
What happens when you take differences between differences, and so on?
This code is beginner-level and for demonstration purposes only. Original ranges should be preserved.
Additional challenge for fun is to keep the script's line count at exactly 100.
"""

import math

PADDING = 4 # For result display
MIN_POWER = 2
MAX_POWER = 16
SCI_NOT_POWER = 11 # Below this number, results will be displayed in a standard notation
NUM_LOW = 1
NUM_HIGH = 21 # Highest number for which the results will be calculated

def get_power_from_user():
    # Prompt the user for an exponent between MIN_POWER and MAX_POWER, inclusive
    while True:
        try:
            power = int(input(f"\nEnter an exponent ({MIN_POWER} to {MAX_POWER}, inclusive): "))
            if MIN_POWER <= power <= MAX_POWER:
                return power
            print(f"Out of range. Please enter a number between {MIN_POWER} and {MAX_POWER}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def calculate_differences(numbers, power):
    # Calculate consecutive differences of numbers raised to the given power
    powered_numbers = [num ** power for num in numbers]
    differences = {}
    current_diffs = powered_numbers

    level = 0
    while len(set(current_diffs)) > 1:
        current_diffs = [current_diffs[i] - current_diffs[i - 1] for i in range(1, len(current_diffs))]
        level += 1
        differences[level] = current_diffs

    return powered_numbers, differences

def format_number(num, level, power):
    # Dynamically format number based on the original power
    if power < SCI_NOT_POWER:
        # For numbers derived from powers less than SCI_NOT_POWER, use standard notation
        return f"{num:,}"
    else:
        # For larger numbers, use scientific notation
        return f"{num:.2e}"

def calculate_max_widths(numbers, powered_numbers, differences, power):
    # Calculate maximum width for each column to ensure proper alignment and spacing
    max_widths = [len(str(max(numbers)))]  # Width of the 'Number' column
    all_numbers = [powered_numbers] + list(differences.values())

    for level, nums in enumerate(all_numbers, start=1):
        formatted_numbers = [format_number(num, level, power) for num in nums]
        max_width = max(len(num) for num in formatted_numbers) + PADDING
        max_widths.append(max_width)

    return max_widths

def display_results(numbers, powered_numbers, differences, power):
    # Display the numbers, their powers, and all levels of differences with
    max_widths = calculate_max_widths(numbers, powered_numbers, differences, power)

    # Headers
    headers = ["Number", "Power"] + [f"Diff_{i}" for i in range(1, len(differences) + 1)]
    for i, header in enumerate(headers):
        print(f"{header.ljust(max_widths[i])}", end=" ")
    print()

    # Rows
    for i, num in enumerate(numbers):
        formatted_number = str(num).ljust(max_widths[0])
        print(f"{formatted_number}", end=" ")

        for level, nums in enumerate([powered_numbers] + list(differences.values()), start=1):
            if i < len(nums):
                formatted_num = format_number(nums[i], level, power).rjust(max_widths[level])
                print(f"{formatted_num}", end=" ")
            else:
                print(" " * max_widths[level], end=" ")
        print()

def main():
    power = get_power_from_user()
    numbers = list(range(NUM_LOW, NUM_HIGH))
    powered_numbers, differences = calculate_differences(numbers, power)
    display_results(numbers, powered_numbers, differences, power)

    # Explaining the results
    fact = math.factorial(power)
    print(f"\nConstant differences always appear at level equal to the exponent (here {len(differences)}).")
    print(f"The constant difference is always the factorial of the exponent ({power}! = {fact}).")

if __name__ == "__main__":
    main()

# Copyright (c) [2023] [vccjlc]
