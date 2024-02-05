# Quick Sort


def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]  # choose the mid element as a pivot

    left = [n for n in lst if n < pivot]
    middle = [n for n in lst if n == pivot]
    right = [n for n in lst if n > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    lst = [2, 5, 1, 3, 9, 8, 6, 7]
    merged = quick_sort(lst)
    print("Input List: ", lst)
    print("Output List: ", merged)
