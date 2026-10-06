text = "Python is simple. I use Python for analytics. Python is useful."
word = "Python"

first_position = text.find(word)
last_position = text.rfind(word)

first_part = text[:first_position]
main_part = text[first_position:last_position + len(word)]
last_part = text[last_position + len(word):]

print(f"Original text:\n{text}")
print(f"\nWord: {word}  (type={type(word).__name__}, len={len(word)})")
print(f"\nFirst occurrence: {first_position}")                        
print("\nLast occurrence:")
print(last_position)

print("\nText before the first occurrence:")
print(first_part)

print("\nText from the first to the last occurrence:")
print(main_part)

print("\nText after the last occurrence:")
print(last_part)