def nonConsecutive(arr):
    if len(arr) < 2:
          print("None")

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1] + 1:
            print (arr[i])

    return None
result = nonConsecutive([1, 2, 3, 5, 6, 7])
