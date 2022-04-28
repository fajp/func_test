def unique_substr_len(string: str) -> int:
    """
    Find the length of the longest substring
    without repeating characters in the given string
    """

    substring = ""
    max_unique = ""

    for i, char in enumerate(string):
        if char in substring:
            where = substring.find(char)
            substring = substring[where+1:]

        substring += char
        if len(substring) > len(max_unique): max_unique = substring

    return len(max_unique)
