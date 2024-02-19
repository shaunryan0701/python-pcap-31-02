import random

def lottery(ticket_count: int, max_number: int):
    # Returns ticket_count numbers between 1 and max_number
    numbers = []
    for i in range(max_number):
        numbers.append(i)

    unique_numbers = random.sample(numbers, ticket_count)
    return (unique_numbers, random.choice(unique_numbers) )  

print(lottery(6, 49)) # ([1, 2, 3, 4, 5, 6], 3)