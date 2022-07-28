def valid_parentheses(s):
    if float(int(len(s)/2)) != len(s)/2:
        return False

    return remove_parentheses(s, 0)


def remove_parentheses(st, i):
    parentheses_mapping = {'(': ')', '{': '}', '[': ']'}
    opening = '[{('
    if i < 0:
        i = 0
    elif i >= len(st)/2:
        return False
    if st[i] in opening and st[i+1] == parentheses_mapping[st[i]]:
        st = st[:i] + st[i + 2:]
        if len(st) > 0:
            return remove_parentheses(st, i - 1)
        else:
            return True
    elif st[i] in opening:
        return remove_parentheses(st, i + 1)
    elif st[i] not in opening:
        return False

print(valid_parentheses('()()())'))
print(valid_parentheses('()()()'))
print(valid_parentheses('((()))'))
print(valid_parentheses('((((((()'))
print(valid_parentheses('(([]){{[()]}}))'))
print(valid_parentheses('(([]{{[()]}}))'))
print(valid_parentheses('(('))
