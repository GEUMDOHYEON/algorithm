S = input()
key = input()

result = ''

for i in range(len(S)):
  if S[i] == ' ':
    result += ' '
  else:
    result += chr((ord(S[i]) - ord(key[i%len(key)]) - 1) % 26 + ord('a'))

print(result)