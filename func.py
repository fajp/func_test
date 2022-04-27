def unique_substr_len(string: str) -> int:
    """
    Find the length of the longest substring
    without repeating characters in the given string
    """

    chars = []
    length = 0
    max_length = 0

    for char in string:

        if char in chars:
            length = 0
            chars.clear()

        chars.append(char)
        length += 1
        if length > max_length: max_length = length

    return max_length
