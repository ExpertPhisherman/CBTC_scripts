def max_ASCII_avg(ascii_str):
    words = ascii_str.split()
    max_avg = 0
    for word in words:
        word_filtered = filter(str.isalpha, word)
        max_avg = max(max_avg, sum([ord(char) for char in word_filtered]))
    return max_avg

print(max_ASCII_avg("Hello, how are you? That is nice to hear!"))