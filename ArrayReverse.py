scores = [6, 5, 4, 3, 2, 1]
start, end = 0, len(scores) - 1
while start < end:
    scores[start], scores[end] = scores[end], scores[start]
    start += 1
    end -= 1
print('Swapped:', scores)

# output:
# Swapped: [50, 40, 30, 20, 10]