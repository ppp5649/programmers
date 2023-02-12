# reference 개념
# a=1이란 a라는 변수가 1이라는 객체를 참조(reference)한다는 의미이다.

# a = 1
# b = "Hello"
# c = [1, 2, 3, 4, 5]

# print(id(a))
# print(id(b))
# print(id(c))


# ==================================
# # immutable 객체 (int, float, bool, string, tuple)
# a = 1  # a라는 변수는 1이라는 객체를 참조한다.
# b = a  # b라는 변수는 a를 참조하므로 동일하게 1이라는 객체를 참조한다.
# print(id(a), id(b))  # 즉, a와 b는 동일한 객체를 참조하며 id값도 같다.
# print(a is b)  # is 연산자는 동일한 객체인지 판단한다.
# print(a == b)  # == 연산자는 동일한 값인지 판단한다.
# print(a, b)

# b = 2
# print(id(a), id(b))  # b는 2라는 객체를 참조하므로 당연히 id값이 다르다.
# print(a is b)
# print(a, b)


# ==================================
# # mutable 객체 (list, dict, set)

# a = [1, 2, 3]
# b = a
# print(id(a), id(b))
# print(a, b)
# print(a is b)
# b[0] = 10
# # [1, 2, 3] 객체를 참조하다가 [10, 2, 3] 객체를 새롭게 참조하는 것이 아닌 리스트 객체의 값을 바꿔줌으로써 새로운 참조가 일어나지 않음


# print(id(a), id(b))  # 여전히 a와 b는 같은 객체를 참조하고 있음 (id값 동일)
# print(a, b)


# ==================================
# a = [1, 2, 3]
# b = a[:]  # b는 a와 같은 [1,2,3] 이지만 둘은 다른 객체를 참조 하고있다.
# # 위의 과정은 얕은 복사(copy) 과정이다.
# print(a, b)
# print(a is b)  # False
# print(a == b)  # True

# a[0] = 10  # a의 값만 변경됨
# print(a, b)


# ==================================
# deep copy의 개념을 이해해야 알 수 있음
from copy import copy

a = [[1, 2, 3], [4, 5, 6]]
b = copy(a)
a[0][0] = 10
print(a, b)  # a와 b값이 같음 a[0][0]와 b[0][0]가 모두 변경됨
print(a is b)  # False
