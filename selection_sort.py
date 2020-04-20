"""selection sort, yielding swap pairs"""


def selection_sort(l: list):
    list_length = len(l)

    for swap_index in range(0, list_length):
        min_value = l[swap_index]
        min_index = swap_index

        for item_index in range(swap_index, list_length):
            if (item_value := l[item_index]) < min_value:
                min_value, min_index = item_value, item_index

        l[swap_index], l[min_index] = l[min_index], l[swap_index]
        yield (swap_index, min_index)


if __name__ == '__main__':
    from random import randint
    l = [randint(0, 1000) for _ in range(0, 1000)]
    s = sorted(l)

    print(l)

    print(f'sorted: {l == s}')

    for pair in selection_sort(l):
        print(pair)

    print(l)
    print(f'sorted? {l == s}')