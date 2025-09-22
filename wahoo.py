def count_letters(word):
    mydictionary = {}
    for c in word:
        if c in mydictionary:
                mydictionary[c] += 1
        else:
                mydictionary[c] = 1
    print(mydictionary)

count_letters("skibidi rizz")


    