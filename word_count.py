#word count version 1

from collections import Counter

with open('peter_rabbit.txt', 'r', encoding = 'utf-8') as file:

    word_count = Counter(file.read().lower().split()).most_common(10)
    print("*****Peter Rabbit's Top 10 Words*****")
    for key, value in word_count:
        print(key, '--->', value)
