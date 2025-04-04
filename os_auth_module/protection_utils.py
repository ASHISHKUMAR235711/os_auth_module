import re

# Sanitize user input to prevent injections or escape characters
def sanitize_input(input_str):
    # Allow only alphanumeric characters and a few safe symbols
    sanitized = re.sub(r"[^\w@.-]", "", input_str)
    return sanitized

# Simulate trapdoor detection (very basic check for suspicious usernames)
def trapdoor_check(input_str):
    suspicious_keywords = ["admin", "root", "system", "null"]
    for keyword in suspicious_keywords:
        if keyword in input_str.lower():
            raise ValueError("Trapdoor keyword detected in input.")

# Simulate buffer overflow detection (e.g., unusually long input)
def is_buffer_overflow(input_str, limit=64):
    return len(input_str) > limit
