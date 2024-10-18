#1
result1 = [x for x in range(1,1001) if x % 7 == 0]

#2
result2 = [x // 3 if x % 3 == 0 else int(f"{x}{x}") for x in range(1, 1001)]

#3
my_string = "  hel l o      world   "
spaces_count = sum(1 for char in my_string if char == ' ')

#4
text = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
words_with_y = [word for word in text.split() if word.lower().startswith('y')]

#5
result3 = [(index, char) for index, char in enumerate("hi, 3.44, 535  ")]

#6
text = "In 1984 there were 13 instances of a protest with over 1000 people attending"
result4 = [int(word) for word in text.split() if word.isdigit()]

#7
numbers_type = ("четное" if i % 2 == 0 else "нечетное" for i in range(1, 21))
result_list = list(numbers_type)

#8
text = "The trickiest part of learning list comprehension for me was really understanding the syntax."
short_words = [word for word in text.split() if len(word) < 4]

#9
prime_numbers = (
    num for num in range(2, 51)
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1))
)