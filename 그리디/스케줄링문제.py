N = int(input())

tlst = []
for _ in range(N):
    tlst.append(tuple(map(int, input().split())))

tlst = sorted(tlst, key=lambda x:(x[1],x[0]))
curtime=0
cnt=0
for s, e in tlst:
    if s>=curtime:
        cnt+=1
        curtime = e

print(cnt)