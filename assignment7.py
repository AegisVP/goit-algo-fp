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
        analytical_prob = {2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36, 6: 5 / 36, 7: 6 / 36, 8: 5 / 36, 9: 4 / 36, 10: 3 / 36, 11: 2 / 36, 12: 1 / 36}
        print()
        print('Value | Count       | Probab MC   | Probab AN   ')
        print('------|-------------|-------------|-------------')

        for i in range(1, 12+1):
            if i in probabilities:
                print(f"{i:^6}| {counts[i]:<12}| {probabilities[i]:<12.5f}| {analytical_prob[i]:.5f}")

    return probabilities


if __name__ == '__main__':
    start_time = timeit.default_timer()
    tries = 5_000_000
    print(f"Starting with {tries} throws...")
    dice_results = throw_dice(tries)
    calculate_probabilities(dice_results, True)
    print("\n\nFinished.\nIt took {time} seconds.".format(time=timeit.default_timer() - start_time))
