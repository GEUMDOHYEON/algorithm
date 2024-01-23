import sys

N = int(sys.stdin.readline())
count = 0
n = N

while True:
    n_1 = n % 10
    n_10 = n // 10
    sum = (n_1 + n_10) % 10
    n = (n_1 * 10) + sum
   
    count += 1

    if n == N:
        print(count)
        break
    
    

# N = input()

# n1, n2 = 0, 0
# count = 0

# if int(N) < 10:
#     n1 = '0'
#     n2 = N
#     N = n1 + n2 
# else:   
#     n1 = N[0]
#     n2 = N[1]

# def plus(n1,n2):
#     global count
    
#     n = int(n1) + int(n2)

#     if n < 10:
#         a = '0'
#         b = str(n)
#     else:
#         a = str(n)[0]
#         b = str(n)[1]

#     count += 1

#     if n2 + b == N:
#         return count
    
#     return plus(n2,b)

# print(plus(n1,n2))


# import sys

# # ----------

# def plus(nStr):
#     global count

#     count += 1

#     n = int(nStr)
#     n_10 = nStr[0]
#     n_1 = nStr[1]

#     # if n < 10:
#     #     newStr = str(n)
#     # else:
#     #     newStr = n_1

#     currentNumberSum = str(int(n_10) + int(n_1))
#     checkStr = f"{n_1}{currentNumberSum[len(currentNumberSum) - 1]}"

#     if checkStr == N:
#         return count

#     return plus(checkStr)

# # ----------

# # main
# N = sys.stdin.readline().strip()

# n1, n2 = '', ''
# count = 0

# if int(N) < 10:
#     N = f"0{N}"

# print(plus(N))