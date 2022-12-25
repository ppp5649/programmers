# # 중복값 제거 여러가지 방법

dup_list = [30, 5043, 32, 111, 111, 594, 4, 594]

## 순서 유지 X ###
# solution1) set 자료구조 사용

# Set 자료구조의 특징
# 1. 중복을 허용하지 않는다.
# 2. 순서가 유지되지 않는다. (순서랜덤)


unique_list = list(set(dup_list))
print(unique_list)

## 순서 유지 O ###
# soultion2) for문 이용
unique_list = []


# solution3) dict.fromkeys() - 파이썬 3.6 이전에는 순서대로 key값이 저장되지 않았음
# dict에 list를 씌우면 key값으로 list가 생성된다.

unique_list = list(dict.fromkeys(dup_list))
print(unique_list)

# solution4) OrderedDict.fromkeys() - 파이썬 모든 버전에서 순서대로 key값 저장
from collections import OrderedDict

unique_list = list(OrderedDict.fromkeys(dup_list))
print(unique_list)



