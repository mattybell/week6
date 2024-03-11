def count_substring(substring, memory):
    """Print the number of occurrences of substring."""
    if substring:
        count = memory.count(substring)
        print(f"Substring '{substring}' count: {count}")
    else:
        print("Error: Missing argument for 'count' command.")
