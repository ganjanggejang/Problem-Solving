"""
테이블 정의하기
d[i][j] = 현재 1이 j번 연속 등장한, 길이가 i인 이친수

점화식 찾기
d[i][0] = d[i-1][0] + d[i-1][1]
d[i][1] = d[i-1][0]

초기값 설정하기
d[1][0] = 0
d[1][1] = 1

"""
n = int(input())
d = [[0] * 2 for _ in range(n + 1)]
d[1][0] = 0
d[1][1] = 1

for i in range(2, n + 1):
    d[i][0] = d[i - 1][0] + d[i - 1][1]
    d[i][1] = d[i - 1][0]

print(sum(d[n]))
