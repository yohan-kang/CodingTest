n, m = map(int, input().split() )

d = [[0] * m for _ in range(n)]

x,y,direction = map(int, input().split())


# 처음 좌표를 0 육지로 두지 않고 , 의미를 다르게 방문 처리 표시로 1을 한다 
# 조건 : 이미 가본 칸이거나 바다로 되어 있는 경우 
d[x][y] = 1 

array = []
for i in range(n):
	array.append(list(map(int, input().split())))
	

#북 동 남 서  지정
dx = [-1,0,1,0]
dy = [0,1,0,-1]


def trun_left()  :

	# global 키워드 사용이유는 함수 바깥에서 사용되었기 떄문이다 
	global direction

	direction += -1
	if direction == -1 : 
			direction = 3 
	
	
count = 1


turn_time = 0


while True :
	
	  turn_left()
	  nx = x + dx[direction]
	  ny = y + dy[direction]
	  
		if array[nx][ny] == 0 and d[nx][ny] == 0 :
			d[nx][ny] == 1
			x = nx
			y = ny
			count +=1 
			turn_time = 0 
			continue 
		
		# 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우 
		else : 
			turn_time += 1
		
		#4방향 모두 갈수 없는 경우
		if turn_time = 4:
		
		
				# # 빼는 이유는 현재 바라보는 방향의 반대 방향으로 이동
				nx = x - dx[direction]
			  ny = y - dy[direction]
				
				# 뒤로 갈수 있다면 이동하기 (육지라면)
				if array[nx][ny] == 0 :
						x = nx
						y = ny
				
				# 뒤가 바다로 막혀 있는 경우 
				else :
					break
			
				# 이거 왜 하지????????	
				turn_time = 0
			
			
			
print(count)
			 

