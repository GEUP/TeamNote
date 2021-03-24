g = [[1,2,3],[0],[0,3],[0,2],[5],[4]] #인접 리스트
m = [0,0,0,0,0,0] #0:방문하지 않음 1: 큐 대기중 2: 방문 완료
q = [] #append(), pop(0)

s = 0

# 함수기능: s노드의 방문하지 않은 이웃 노드를 큐에 넣는다. 큐의 값을 하나씩 pop하면서 너비우선탐색한다.
# 기저조건: 방문하지 않은 이웃 노드가 없는 경우
def bfs(s):
    m[s] = 2
    print(s,'-> ', end = ' ')
    base = False # 방문하지 않은 이웃 노드가 없으면 False
    for x in g[s]:
        if m[x]==0:
            base = True # 방문하지 않은 이웃 노드가 존재한다.
            q.append(x)
            m[x]=1

    if not base:
        return

    while True:
        if len(q) == 0:
            break
        bfs(q.pop(0))

bfs(0)

