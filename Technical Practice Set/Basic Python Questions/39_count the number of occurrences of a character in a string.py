def count_char_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

# Example usage
input_string = "hello world"
character_to_count = 'l'

occurrences = count_char_occurrences(input_string, character_to_count)
print(f"The character '{character_to_count}' appears {occurrences} times in '{input_string}'")
