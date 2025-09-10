str = input("Enter string: ")


freq = {}


for char in str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1


max_char = min(freq, key=freq.get)
max_freq = freq[max_char]

print(f"The character with the lowest frequency is '{max_char}'")