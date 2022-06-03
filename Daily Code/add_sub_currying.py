def StringMatching(str, pattern):
    if any(pattern in s for s in str):
        return True
    return False
print(StringMatching(['Hello Word'], 'ello'))