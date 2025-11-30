def insertion_sort(arr):
    # אלגוריתם מיון בשיטה insertion sort
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # הזזה של איברים גדולים יותר ימינה
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    # קריאת הקלט מקובץ data.txt
    try:
        with open("data.txt", "r") as f:
            # נניח שהמספרים מופרדים ברווחים או שורות
            content = f.read().split()
            numbers = [int(x) for x in content]
    except FileNotFoundError:
        print("file data.txt Not found.")
        return
    except ValueError:
        print("The file contains non-numeric values.")
        return

    # מיון המספרים
    sorted_numbers = insertion_sort(numbers)

    # הדפסת התוצאה – מספר אחד בכל שורה
    for num in sorted_numbers:
        print(num)

if __name__ == "__main__":
    main()

