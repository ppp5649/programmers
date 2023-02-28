# 집합 연산은 산술 연산자와 논리 연산자를 사용한다.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 합집합 (|) - OR 연산

print(a | b)  # {1, 2, 3, 4, 5, 6}
print(set.union(a, b))  # {1, 2, 3, 4, 5, 6}

# 교집합 (&) - AND 연산

print(a & b)  # {3, 4}
print(set.intersection(a, b))  # {3, 4}

# 차집합 (-) - 뺄셈 연산

print(a - b)  # {1, 2}
print(set.difference(a, b))  # {1, 2}

# 대칭 차집합 (^) - XOR 연산

print(a ^ b)  # {1, 2, 5, 6}
print(set.symmetric_difference(a, b))  # {1, 2, 5, 6}
