# 집의 수 입력
n = int(input())

# 집 위치 입력
location = list(map(int, input().split()))

# 오름차순으로 정렬
location.sort()

# 최솟값 출력
result = location[(n-1)//2]
print(result)