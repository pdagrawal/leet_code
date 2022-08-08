def ransom_note(ransomNote, magazine):
    char_hash = {}
    for char in magazine:
        if char in char_hash:
            char_hash[char] += 1
        else:
            char_hash[char] = 1

    for char in ransomNote:
        if char in char_hash and char_hash[char] > 0:
            char_hash[char] -= 1
        else:
            return False

    return True


print(ransom_note('a', 'b'))
print(ransom_note('a', 'ab'))
print(ransom_note('aa', 'aab'))
print(ransom_note('aaaa', 'aaaa'))
