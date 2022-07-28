def valid_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

print(valid_anagram('anagram', 'nagaram'))
print(valid_anagram('rat', 'car'))
