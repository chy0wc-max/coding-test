# 4. K번째 수 - 정렬

# [문제설명]
# 배열 array와 명령 배열 commands가 주어집니다.
# 각 명령 [i, j, k]는 "array의 i번째부터 j번째까지 자른 뒤
# 정렬했을 때 k번째 수"를 의미합니다(모두 1부터 세는 1-indexed).
# 각 명령의 결과를 순서대로 담아 반환하세요.

# [제한사항]
# array의 길이: 1 ~ 100
# commands 길이: 1 ~ 50

# [입출력 예]
#
# nums
# [1,5,2,6,3,7,4]
# 
# commands
# [[2,5,3],[4,4,1],[1,7,3]]
#
# return
# [5,6,3]

# 풀이
def solution(array, commands):
    result = list()
    for i, j, k in commands:
        result.append(sorted(array[i-1:j])[k-1])
    return result

print(solution([1,5,2,6,3,7,4], [[2,5,3],[4,4,1],[1,7,3]]))