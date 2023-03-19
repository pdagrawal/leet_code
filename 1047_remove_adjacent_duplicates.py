def removeDuplicates(s: str) -> str:
    # i = 0
    # while i <= len(s)-2:
    #     if len(s) == 1:
    #         return s
    #     elif s[i] == s[i+1]:
    #         s = s[:i] + s[i+2:]
    #         i = max(0, i-1)
    #     else:
    #         i += 1
    # return s
    output = []
    for ch in s:
        if output and ch == output[-1]:
            output.pop()
        else:
            output.append(ch)
    return ''.join(output)

print(removeDuplicates('aaaaaasaasasaa'))