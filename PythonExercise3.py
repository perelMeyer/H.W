def main():
    # ôúéçú ä÷åáõ ì÷øéàä
    with open("data3.txt", "r") as f:
        # ÷øéàú äùåøåú åäîøúï ìîñôøéí ùìîéí
        numbers = [int(line.strip()) for line in f if line.strip()]

    # áãé÷ä ùä÷åáõ àéðå øé÷
    if not numbers:
        print("file empty.")
        return

    # àúçåì òøëé îéðéîåí åî÷ñéîåí ìòøê äøàùåï
    minimum = numbers[0]
    maximum = numbers[0]

    # îòáø òì ùàø äîñôøéí åòãëåï òøëéí
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    # äãôñú äúåöàä
    print(f"min={minimum}")
    print(f"max={maximum}")

if __name__ == "__main__":
    main()

