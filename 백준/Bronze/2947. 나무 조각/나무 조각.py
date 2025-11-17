arr = list(map(int, input().split()))
tmp = 0

for _ in range(5):

  for i in range(len(arr)-1):

    if arr[i] > arr[i+1]:
      tmp = arr[i]
      arr[i] = arr[i+1]
      arr[i+1] = tmp
      
      for a in arr:
        print(a, end=" ")
      print()