### Bubble Sort ###


def bubble_sort(arr):

    length = len(arr)

    for i in range(length - 1):
        print("\n")
        print("i: ", i)
        # 한바퀴 돌때마다 맨끝 요소 하나씩 정렬 할 필요 없어지므로 -i
        for j in range(length - 1 - i):
            print("j: ", j)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort([2, 3, 1, 5, 4]))
