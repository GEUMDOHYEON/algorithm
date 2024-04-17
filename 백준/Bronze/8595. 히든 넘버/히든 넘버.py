N = int(input())

word = input()
result = 0
tmp = []

for i in word:
    if i.isdigit():
        tmp.append(i)
    else:
        if tmp:
            t = ('').join(tmp)
            result += int(t)
            tmp = []
if tmp:
    t = ('').join(tmp)
    result += int(t)
    tmp = []
    
print(result)