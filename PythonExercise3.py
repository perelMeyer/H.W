def main():
    # פתיחת הקובץ לקריאה
    with open("data.txt", "r") as f:
        # קריאת השורות והמרתן למספרים שלמים
        numbers = [int(line.strip()) for line in f if line.strip()]

    # בדיקה שהקובץ אינו ריק
    if not numbers:
        print("file empty.")
        return

    # אתחול ערכי מינימום ומקסימום לערך הראשון
    minimum = numbers[0]
    maximum = numbers[0]

    # מעבר על שאר המספרים ועדכון ערכים
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    # הדפסת התוצאה
    print(f"min={minimum}")
    print(f"max={maximum}")

if __name__ == "__main__":
    main()

