#문제: 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.
#아이디어 찾기: 그래프로 그려보자
T = int(input())
for _ in range(T):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(tuple(map(int, input().split())))

    lst.sort()
    # 서류 점수 1등 x0는 합격하고 x0보다 면접 점수가 낮은 사람은 모두 탈락한다.
    # x0보다 면접 점수가 높은 사람 중 서류 점수가 가장 높은 사람 x1은 합격하고 x1보다 면접 점수가 낮은 사람은 모두 탈락한다.
    # x1보다 면접 점수가 높은 사람 중 서류 점수가 가장 높은 사람 x2는 합격하고 x2보다 면접 점수가 낮은 사람은 모두 탈락한다.
    # ...
    min = lst[0][1] # x1의 면접 점수
    cnt = 1
    for x in lst[1:N]:
        if min > x[1]:
            min = x[1]
            cnt += 1

    print(cnt)


