#An = 동전의 가치 A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수
N, K = map(int, input().split())
COINS = []
for _ in range(N):
    COINS.append(int(input()))
COINS.sort(reverse=True)
cnt = 0
for coin in COINS:
    if coin>K:
        continue
    while K>=coin:
        K-=coin
        cnt +=1
print(cnt)
