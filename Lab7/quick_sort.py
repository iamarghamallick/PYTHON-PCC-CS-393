# Quick Sort

def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]

    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    lst = [2, 5, 1, 3, 9, 8, 6, 7]
    merged = quick_sort(lst)
    print("Input List: ", lst)
    print("Output List: ", merged)
