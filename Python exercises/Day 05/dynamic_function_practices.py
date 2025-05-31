def all_positives(numbers):
    for n in numbers:
        if n < 0:
            return False
    return True

print(all_positives([100, 100, 13, 45, -67, 89]))
