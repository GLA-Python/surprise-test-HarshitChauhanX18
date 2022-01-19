def pattern(p):
    result = []
    i = 0
    while i < len(p):
        count = 1
        while i + 1 < len(p) and p[i] == p[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + p[i])
        i += 1
    return ''.join(result)


A = int(input())
N = 1
for i in range(A):
    print(N)
    number = pattern(str(N))
