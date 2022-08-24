def heightChecker(heights):
    expected = sorted(heights)
    counter = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            counter += 1
    return counter

print(heightChecker([1,1,4,2,1,3]))
