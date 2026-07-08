# 2. 두 개 뽑아서 더하기 - 완전탐색/조합

# [문제설명]
# 정수 배열 numbers에서 서로 다른 인덱스에 있는 두 수를 뽑아 
# 더할 수 있는 모든 값을, 중복 없이 오름차순으로 정렬해 반환하세요.

# [제한사항]
# numbers의 길이: 2 ~ 100
# 각 원소: 0 ~ 100

# [입출력 예]
#
# numbers
# [2,1,3,4,1]
# [5,0,2,7]
#
# result
# [2,3,4,5,6,7]
# [2,5,7,9,12]

# 풀이
# 서로 다른 인덱스에 있는 두 수를 뽑아 더할 수 있는 모든 값: 조합
# 중복 없이 오름차순으로 정렬: set, sorted

from itertools import combinations

def solution(numbers):
    return sorted(set([a + b for a, b in combinations(numbers, 2)]))

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))

