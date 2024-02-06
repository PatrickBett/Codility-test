def toRange(arr):
    ranges = []
    i = 0
    while i < len(arr):
        start = arr[i]
        while i < len(arr) - 1 and arr[i] + 1 == arr[i + 1]:
            i += 1
        end = arr[i]
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}_{end}")
        i += 1
    return ','.join(ranges)

def toArray(s):
    if not s:
        return []
    
    result = []
    ranges = s.split(',')
    
    for r in ranges:
        if '_' in r:
            start, end = map(int, r.split('_'))
            result.extend(range(start, end + 1))
        else:
            result.append(int(r))
    
    return result

# Test cases
arr1 = [5, 6, 7, 8, 9]
range_str1 = toRange(arr1)
print(range_str1)  # Output: "5_9"
print(toArray(range_str1))  # Output: [5, 6, 7, 8, 9]

arr2 = [6]
range_str2 = toRange(arr2)
print(range_str2)  # Output: "6"
print(toArray(range_str2))  # Output: [6]

arr3 = [3, 4, 5, 6, 9]
range_str3 = toRange(arr3)
print(range_str3)  # Output: "3_6,9"
print(toArray(range_str3))  # Output: [3, 4, 5, 6, 9]
