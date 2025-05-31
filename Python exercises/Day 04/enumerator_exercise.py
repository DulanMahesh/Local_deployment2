#Print to the screen only the indices of those names in the list below, that start with M:

list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]

for index, n in enumerate(list_names):
    if n.startswith("M"):
        print(index)
    else:
        continue
        