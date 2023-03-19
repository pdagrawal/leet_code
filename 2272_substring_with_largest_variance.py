from collections import defaultdict

def largestVariance(s: str) -> int:
    ans = 0
    memo = set()
    c = defaultdict(int)
    for i in range(len(s)):
        c.clear()
        for v in range(i, min(len(s), i+ans+1)):
            c[s[v]] += 1
        print(c)
        for j in range(i+1+ans, len(s)):
            c[s[j]] += 1
        max_ = max(c.values())
        if max_ < ans + 1:
            continue
        min_ = min(c.values())
        h = (max_, min_)
        if h in memo:
            continue
        memo.add(h)
        print('Memo', memo)
        ans = max(ans, max_ - min_)
        print(c)
    return ans

# 3
print(largestVariance('aababbb'))