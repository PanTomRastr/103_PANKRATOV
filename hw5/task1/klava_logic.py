import random


def simulator(time_one, time, your_bag):
    count_test = time // time_one
    for i in range(count_test):
        if random.randint(1, 100) < your_bag + 1:
            return 'L'
    if random.randint(1, 100) < your_bag + 1:
        return 'S'
    return 'F'
