# 5. 기능 개발 - 스택/큐

# [문제설명]
# 각 기능의 현재 진도 progresses와 하루당 작업 속도 speeds가 주어집니다.
# 각 기능은 진도가 100 이상이면 완성입니다. 단, 앞에 있는 기능이 먼저
# 완성되어야 뒤 기능도 함께 배포됩니다(배포는 하루에 한 번).
# 각 배포마다 몇 개의 기능이 배포되는지 순서대로 반환하세요.

# [제한사항]
# 작업 개수: 1 ~ 100
# 진도: 0 ~ 99
# 속도: 1 ~ 100

# [입출력 예]
#
# progresses
# [93,30,55]
# [95,90,99,99,80,99]
#
# speeds
# [1,30,5]
# [1,1,1,1,1,1]
#
# return
# [2,1]
# [1,3,2]

# 풀이
# progresses = [93,30,55]
# speeds = [1,30,5]
# 
# 각 기능들이 배포까지 몇일이 걸리는가? 
# (100 - progresses[i]) / speeds[i]
# 
# 각 기능별 배포까지 일수
# days = [7, 3, 9]
# 
# 즉, 7일에 배포되는 기능은 3일에 배포되는 기능과 함께 배포된다.
# 9일에는 남은 기능 하나가 따로 배포된다.
# 따라서 [2, 1]이다.

import math

def solution(progresses, speeds):
    result = list()
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    front = days[0] # 7
    count = 1

    for d in days[1:]:
        if front >= d:
            count += 1
        else:
            result.append(count)
            count = 1
            front = d
    result.append(count)     
    return result

print(solution([93,30,55], [1,30,5]))
print(solution([95,90,99,99,80,99], [1,1,1,1,1,1]))