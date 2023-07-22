def reverse_seq(n):
    rev = []
    for i in range(n, 0, -1):
        rev.append(i)

    return rev

def reverseseq(n):
    return list(range(n, 0, -1))

print(reverse_seq(5))
print(reverseseq(5))
