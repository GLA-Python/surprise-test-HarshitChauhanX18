def pattern(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i+1 < len(s) and s[i]==s[i+1]:
            i += 1 
            count += 1 
        result.append(str(count)+s[i])
        i += 1 
    return ''.join(result)
    
rows = int(input())
number = 1
for i in range (rows):
    print(number)
    number = pattern(str(number))
