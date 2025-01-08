def count_inversions(arr):
    n = len(arr)
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions
n = int(input("輸入陣列元素的個數: "))
arr = list(map(int, input("輸入陣列元素 (以空格分隔): ").split()))
if len(arr) != n:
    print("輸入的元素數量與指定的個數不符！")
else:
    result = count_inversions(arr)
    print(f"倒轉成對的數量為: {result}")
