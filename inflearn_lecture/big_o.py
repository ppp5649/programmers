### Big O 표기법 ###
def big_o1(n):
    print(n*n)

big_o1(12)

# 2N번 3N번 4N번 실행되더라도 여전히 복잡도는 O(n)
def big_oN(arr):
    for arr_item in arr :
        print(arr_item*arr_item)

big_oN([1,2,3,4])

# O(1) < O(log N) < O(N) < O(Nlog N) < O(N^2)

