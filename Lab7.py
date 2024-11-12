def compress_string(word):
    comp = ""
    while word:
        # Find the maximum length prefix of a single character c repeating at most 9 times
        c = word[0]
        count = 1
        while count < 9 and count < len(word) and word[count] == c:
            count += 1
        # Append the length of the prefix followed by the character to comp
        comp += str(count) + c
        # Remove the prefix from word
        word = word[count:]
    return comp

# Example usage:
print(compress_string("abcde"))  # Output: "1a1b1c1d1e"
print(compress_string("aaaaaaaaaaaaaabb"))  # Output: "9a5a2b"
