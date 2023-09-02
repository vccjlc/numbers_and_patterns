# Raise consecutive natural numbers to any power and observe differences between results.
# What happens when you take differences between differences, and so on?
import math

# Take the exponent from the user.
while True:
    try:

        power = int(input("\nPlease enter the exponent (between 2 and 16, inclusive): "))

        if not 2 <= power <= 16:
            print("Please enter an integer between 2 and 16. Try, try again my friend.")
            continue  # Restart the loop

        break

    except ValueError:
        print("Invalid input. Please enter an integer.")


# Function to find powers, differences and display the results stored in a dictionary
def find_constant_diff(n, power):
    numbers = list(range(1, n + 1))
    powered_numbers = [i ** power for i in numbers]
    differences = [powered_numbers[i] - powered_numbers[i - 1] for i in range(1, len(powered_numbers))]

    data = {'Number': numbers, 'Power': powered_numbers, 'Difference_1': differences}

    diff_level = 1

    while True:
        last_diff_key = f"Difference_{diff_level}"
        new_diff_key = f"Difference_{diff_level + 1}"

        last_diffs = data[last_diff_key]
        new_diffs = [last_diffs[i] - last_diffs[i - 1] for i in range(1, len(last_diffs))]

        data[new_diff_key] = new_diffs

        if len(set(new_diffs)) == 1:
            break

        diff_level += 1

    # Display the results
    print("Number", end="")
    for key in data.keys():
        if key != "Number":
            print(f"{key:>15}", end="")
    print()

    for i in range(n):
        print(f"{data['Number'][i]:>7}", end="")
        for key in list(data.keys())[1:]:
            if i < len(data[key]):
                print(f"{data[key][i]:>15}", end="")
            else:
                print(" " * 15, end="")
        print()


# Call the function
find_constant_diff(20, power)


# Explain the results
fact = math.factorial(power)
print(f"\nThe number of differences is equal to the exponent ({power})")
print(f"The final differences are equal to exponent factorial ({power}! = {fact})")

# Copyright (c) [2023] [vccjlc]