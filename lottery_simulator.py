# Lottery Simulator


from random import randint

d
def generate_numbers(n): # Generate winning numbers
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers

def draw_winning_numbers(): # Generate a bonus number
    winning_numbers = generate_numbers(7)

    return sorted(winning_numbers[:6]) + winning_numbers[6:]

def count_matching_numbers(numbers, winning_numbers): # Count the number of matching numbers
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count += 1

    return count

def check(numbers, winning_numbers): # Calculate the reward

    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000


















