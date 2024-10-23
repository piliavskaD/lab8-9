import string

strings = input("Enter varios symbols: ")

num_c = 0
eng_letter_c = 0
punct_c = 0
ukr_letter_c = 0


set_eng = set()
set_ua = set()

for word in strings:
    if word.isdigit():
        num_c += 1
    elif word in string.ascii_letters:
        eng_letter_c += 1
        set_eng.add(word)
    elif word in string.punctuation:
        punct_c += 1
    elif "А" <= word <= "Я" or "а" <= word <= "я":
        ukr_letter_c += 1
        set_ua.add(word)


print(f"Number of digit: {num_c}")
print(f"Number of english letter: {eng_letter_c}")
print(f"Number of punctuation: {punct_c}")
print(f"Number of ukrainian letter: {ukr_letter_c}")
print(f"Ukrainian letter: {set_ua}")
print(f"English letter: {set_eng}")
