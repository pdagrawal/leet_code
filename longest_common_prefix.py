def longest_common_prefix(strs):
    min_str = min(strs, key=len)
    max_lim = len(min_str)
    common = ''
    should_add = True
    for c in range(max_lim):
        print(common)
        for i in range(len(strs)):
            if min_str[c] != strs[i][c]:
                should_add = False
        if should_add:
            common += min_str[c]
        else:
            return common
    return common

print('Final: ', longest_common_prefix(["flower","flow","fl"]))
print('Final: ', longest_common_prefix(["dog","racecar","car"]))
