COINS = [500, 100, 50, 10, 5, 1]
COINS.sort(reverse=True)
N = int(input())
memo = [0 for _ in range(N+1)]
# 기능: n원을 만들때 사용되는 코인의 개수를 반환하고 그 값을 memo[N]에 저장한다.
# 기저 조건: COINS 리스트에 있는 동전의 값들 중 하나와 n이 같으면 1을 반환한다.
def coinProblem(n):
    if COINS[-1] > n:
        return 987654321
    for COIN in COINS:
        if n == COIN:
            memo[n] = 1
            return 1


    for COIN in COINS:
        x = n-COIN
        if x < 0:
            continue
        if memo[x] == 0:
            memo[x] = coinProblem(x)

    i = 0
    while True:
        if n - COINS[i] < 0:
            i += 1
            continue
        else:
            break
    memo[n] = memo[n-COINS[i]]+1
    for COIN in COINS[1+i:]:
        if n-COIN < 0:
            continue
        memo[n] = min(memo[n], memo[n-COIN]+1)
    return memo[n]


result = coinProblem(N)
if result>987654321:
    result=-1
print(result)
