


text = input()

ln = len(text)//2

result = 1

for i in range(ln):
    if text[i] == text[(i+1)*-1]:
        continue
    else :
        result = 0
        break
print(result)


# 더 쉬운 코드 
word = list(input())
if word == word[::-1] :
    print(1)
else :
    print(0)