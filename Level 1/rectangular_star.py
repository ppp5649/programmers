# 직사각형 별찍기
# 풀이 시간 : 4분


a, b = map(int, input().strip().split(" "))

# 1
for _ in range(b):
    print("*" * a)

# 2
print(("*" * a + "\n") * b)
