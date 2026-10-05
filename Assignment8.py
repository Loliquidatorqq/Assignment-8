text = "Python is simple. I use Python for analytics. Python is useful."
word = "Python"

first_position = text.find(word)
last_position = text.rfind(word)

first_part = text[:first_position]
main_part = text[first_position:last_position + len(word)]
last_part = text[last_position + len(word):]

print("Original text:")
print(text)

print("\nWord:")
print(word)

print("\nFirst occurrence:")
print(first_position)

print("\nLast occurrence:")
print(last_position)

print("\nText before the first occurrence:")
print(first_part)

print("\nText from the first to the last occurrence:")
print(main_part)

print("\nText after the last occurrence:")
print(last_part)