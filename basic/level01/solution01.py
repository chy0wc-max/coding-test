# 1. 완주하지 못한 선수 - 해시

# [문제설명]
# 마라톤 경기에 참여한 선수들의 이름이 담긴 배열 participant와
# 완주한 선수들의 이름이 담긴 배열 completion이 주어집니다. 
# 딱 한 명만 완주하지 못했습니다. 완주하지 못한 선수의 이름을 반환하세요.
# `동명이인이 있을 수 있습니다.`

# [제한사항]
# participant의 길이: 1 ~ 100,000
# completion의 길이: participant의 길이 - 1
# 이름은 1 ~ 20자의 알파벳 소문자, 참가자 중 동명이인 존재 가능

# [입출력 예]
#
# participant
# ["leo", "kiki", "eden"]
# ["mislav", "stanko", "mislav", "ana"]
#
# completion
# ["eden", "kiki"]
# ["stanko", "ana", "mislav"]
# 
# return
# "leo"
# "mislav"

# 풀이1 - collections.Counter를 사용
from collections import Counter

def solution(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
