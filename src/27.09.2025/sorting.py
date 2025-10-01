def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def main():

    try:
        user_input = input("числа: ")
        numbers = list(map(int, user_input.split()))
        print(f"исходный массив: {numbers}")
        sorted_numbers = insertion_sort(numbers.copy())
        print(f"отсортированный массив: {sorted_numbers}")

    except ValueError:
        print("ошибка! вводите только целые числа.")

if __name__ == "__main__":
    main()