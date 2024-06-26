def max_sequence(arr):
    max_sum = 0
    current_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum if max_sum > 0 else 0