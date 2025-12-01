def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # הוספת שארית האלמנטים
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def main():
    # קריאת הקלט מהקובץ
    with open("data.txt", "r") as f:
        # נניח שכל המספרים נמצאים בשורה אחת מופרדים ברווחים
        numbers = list(map(int, f.read().split()))
    
    sorted_numbers = merge_sort(numbers)
    
    # הדפסת המספרים הממוינים – כל מספר בשורה נפרדת
    for num in sorted_numbers:
        print(num)

if __name__ == "__main__":
    main()

