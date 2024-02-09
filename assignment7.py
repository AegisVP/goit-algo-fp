import random
import timeit
from collections import defaultdict


def throw_dice(tries=10_000):
    counts = defaultdict(int)
    for _ in range(tries):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        counts[dice1 + dice2] += 1
    return counts


def calculate_probabilities(counts, do_print=True):
    total = sum(counts.values())
    probabilities = {val: count / total for val, count in counts.items()}

    if do_print:
        print('\nValue | Probability | Count')
        print('------|-------------|---------')

        for i in range(1, 12):
            if i in probabilities:
                print(f"{i:^6}| {probabilities[i]:<12.5f}| {counts[i]}")

    return probabilities


if __name__ == '__main__':
    start_time = timeit.default_timer()
    tries = 5_000_000
    print(f"Starting with {tries} throws...")
    dice_results = throw_dice(tries)
    calculate_probabilities(dice_results, True)
    print("\n\nFinished.\nIt took {time} seconds.".format(time=timeit.default_timer() - start_time))
