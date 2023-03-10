"""
테이블 정의하기
d[i] = i자리 이친수의 개수

점화식 찾기
d[i] = d[i-1] + d[i-2]
# d[i-1]은 d[i]의 마지막 수가 0일 때: d[i-1]의 어떤 수던 간에 끝에 0만 붙이면 됨
# d[i-2]는 d[i]의 마지막 수가 1일 때: d[i-1]의 끝자리는 항상 0이어야 함, 
그런 수들은 d[i-2]가 뭐든간에 상관 없음, 
따라서 d[i-2]의 모든 수에 0, 1을 순서대로 붙인 모든 수가
"d[i]의 마지막 수가 1일 때"에 해당함

초기값 설정하기
d[1] = 1
d[2] = 1


"""
n = int(input())
d = [0] * (n + 1)
d[1] = 1
d[2] = 1

for i in range(2, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
