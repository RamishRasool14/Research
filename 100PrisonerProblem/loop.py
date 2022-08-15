import random


def box_found_in_loop(prisoner_number, boxes_with_numbers, with_strategy=True):
    boxes_with_numbers = list(map(lambda x: x[1], boxes_with_numbers))
    next_box = prisoner_number
    if with_strategy:
        for x in range(50):
            next_box = boxes_with_numbers[next_box]
            if next_box == prisoner_number:
                return True
        return False
    else:
        for next_box in random.sample(range(0, 100), 50):
            if next_box == prisoner_number:
                return True
        return False


def run_single_experiment(boxes_with_numbers):
    for prisoner in [x for x in range(100)]:
        if not box_found_in_loop(prisoner, boxes_with_numbers, with_strategy=True):
            return 0
    return 1


def find_probability():
    number_of_experiments = 10000
    won_game = 0
    for x in range(number_of_experiments):
        boxes_with_numbers = random.sample(range(0, 100), 100)
        boxes_with_numbers = [(x, boxes_with_numbers[x]) for x in range(100)]
        won_game += run_single_experiment(boxes_with_numbers)
    return won_game / number_of_experiments


print(find_probability())
