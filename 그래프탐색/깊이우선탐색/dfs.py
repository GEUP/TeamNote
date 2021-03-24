g = [[1,2,3],[0,4],[0,3],[0,2],[1,5],[4]] #인접 리스트
m = [0,0,0,0,0,0]

s = 0

#기능: s노드부터 s와 이웃한 노드 중 방문하지 않은 노드들을 깊이우선탐색한다.
#기저조건: 이웃한 노드가 모두 방문되었을 경우 반환한다.
def dfs(s):
    m[s] = 1
    print(s,'->', end=' ')
    #기저조건
    t = False #이웃노드가 모두 방문되었으면 False
    for x in g[s]:
        if m[x] == 0:
            t = True #방문되지 않은 노드가 있다.
    if t==False: #모두 방문되었다면
        return

    #함수완성
    for x in g[s]:
        if m[x] == 1:
            continue
        dfs(x)

dfs(s)