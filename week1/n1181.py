n = int(input())

array = []

for i in range(n):
    array.append(input())

array.sort() # 문자열 알파벳 순으로 정렬
array.sort(key=lambda x:len(x)) # 문자열 길이 순으로 정렬

result = []

for i in array: # 문자열 중복값 제거
    if i not in result:
        result.append(i)
# 문자열 중복값 제거 메소드
# result = set(array)

for i in result:
    print(i)


####### 문자열 길이 순대로 정렬을 위해 버블 정렬 이용(시간 복잡도때문에 시간초과로 인해 실패)
# for i in range(n):
#     for j in range(n-i-1):
#         if len(array[j]) > len(array[j + 1]):
#             tmp = array[j]
#             array[j] = array[j+1]
#             array[j+1] = tmp
