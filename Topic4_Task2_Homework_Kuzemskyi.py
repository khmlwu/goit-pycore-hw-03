import random

def get_numbers_ticket(min, max, quantity) -> list:
    if min <1 or max >1000 or min >= max or quantity > (max - min +1):
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 1000, 6)
print("Ваша лотерейна комбінація:",lottery_numbers)