import numpy as np


with open("inputs/in5.txt") as file:
    orders, lists = file.read().split("\n\n")
    order_rules = {}
    for order in orders.split("\n"):
        left_num, right_num = [int(num) for num in order.split("|")]
        if left_num not in order_rules:
            order_rules.update({left_num: {right_num}})
        else:
            order_rules[left_num].add(right_num)
   
    updates = []
    for lst in lists.strip().split("\n"):
        updates.append([int(num) for num in lst.split(",")])

def is_correct_order(update, order_rules):
    correct_order = 1
    for i, update_number in enumerate(update):
        order_rule_nums = order_rules[update_number]
        for update_number_check in update[i + 1:]:
            if update_number_check not in order_rule_nums:
                correct_order = 0
    return correct_order

def sort_incorrect_update(update, order_rules):
    n = len(update)
    correct_order_update = np.zeros(n, dtype = int)
    for update_number in update:
        numbers_after_count = 0
        for number_after in order_rules[update_number]:
            if number_after in update:
                numbers_after_count += 1
        correct_order_update[n - numbers_after_count - 1] = update_number
    return correct_order_update

part1 = 0
incorrect_updates = []
for update in updates:
    if is_correct_order(update, order_rules):
        part1 += update[len(update) // 2]
    else:
        incorrect_updates.append(update)
print(f"The answer to part 1 is {part1}")

part2 = 0
for update in incorrect_updates:
    correct_order_update = sort_incorrect_update(update, order_rules)
    part2 += correct_order_update[len(correct_order_update) // 2]
print(f"The answer to part 2 is {part2}")
