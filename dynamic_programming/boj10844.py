"""
테이블 정의하기
d[i][j] = 길이가 i인 계단수, 마지막에 사용한 수는 j

점화식 찾기
d[i][j] = d[i-1][j-1] + d[i-1][j+1]

초기값 설정하기
d[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
"""
n = int(input())
mod = 1000000000
d = [[0] * 10 for _ in range(n + 1)]
d[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n + 1):
    d[i][0] = d[i - 1][1]
    for j in range(1, 9):
        d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]
    d[i][9] = d[i - 1][8]

print(sum(d[n]) % mod)
