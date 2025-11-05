def calculate_love_score(name1, name2):
    true_count = 0
    for char in name1.lower():
        if char in "true": true_count += 1
    for char in name2.lower():
        if char in "true": true_count += 1
    print(f"true_count:\t{true_count}")
    love_count = 0
    for char in name1.lower():
        if char in "love": love_count += 1
    for char in name2.lower():
        if char in "love": love_count += 1
    print(f"love_count:\t{love_count}")
    print(f"total:\t{true_count + love_count}")


name1 = input("name 1:")
name2 = input("name 2:")
calculate_love_score(name1, name2)