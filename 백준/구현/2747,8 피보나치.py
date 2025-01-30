# 시간 초과 
def fibonacci(n):
    if n == 0:
        return 0  # F(0) = 0
    elif n == 1:
        return 1  # F(1) = 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # F(n) = F(n-1) + F(n-2)
n = int(input())
print(fibonacci(n))



#시간초과 없음
n = int(input())
d = [0] * (n+1) #단순히 재귀적으로 풀 때 과도한 시간이 걸리는 것을 방지하기 위해 dp로 풀어준다.

if n == 1 or n==2:
    print(1)
else:
    d[1] = 1 #인덱스 에러를 해결하기 위해 이렇게 써주어야 한다.
    d[2] = 1
    for i in range(3,n+1):
        d[i] = d[i-1] + d[i-2] # 재귀함수를 이용해 풀이
    print(d[n])