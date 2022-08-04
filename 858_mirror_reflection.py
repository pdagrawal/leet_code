def mirror_reflection(p, q):
    q_total = q
    left = False
    while True:
        if q_total % p == 0:
            even = ((q_total / p) % 2 == 0)
            if left:
                if even:
                    return 2
            else:
                return 0 if even else 1
        q_total += q
        left = not left

print(mirror_reflection(2, 1))
print(mirror_reflection(3, 1))
