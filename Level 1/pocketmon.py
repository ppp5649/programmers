# 해시 LV1. 폰켓몬

# Counter 사용해서 푼 코드
from collections import Counter


def pocketmon(nums):
    count_dict = Counter(nums)
    answer = len(nums) / 2 if len(count_dict) > len(nums) / 2 else len(count_dict)

    return answer


# 내가 예전에 푼 코드
def pocketmon(nums):
    a = int(len(nums) / 2)
    b = len(set(nums))

    if a > b:
        answer = b

    else:
        answer = a

    return answer
