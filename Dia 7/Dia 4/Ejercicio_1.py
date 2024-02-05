def count_pairs(arr, n, k):
    pairs = set()
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) % k == 0:
                pairs.add((min(arr[i], arr[j]), max(arr[i], arr[j])))
    return len(pairs)

T = int(input("Enter the number of test cases: "))
for case in range(T):
    text = input("Enter the values for n and k separated by a space: ")
    nums = input("Enter the list of numbers separated by spaces: ")
    
    n, k = map(int, text.split())
    T_n = [abs(int(num)) for num in nums.split()]
    
    result = count_pairs(T_n, n, k)
    print("Case {}: {}".format(case + 1, result))

