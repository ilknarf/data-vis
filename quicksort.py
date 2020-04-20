"""quicksort that returns swap pairs"""

def quicksort(l: list, lo: int, hi: int):
    """generator that returns pairs of index swaps"""

    # partition middle element (lit says that median is theoretically best)
    i = (lo + hi) // 2
    pivot = l[i]

    left = lo
    right = hi

    while True:
        left_swap = None
        right_swap = None

        for v in range(left, i+1):
            if l[v] > pivot:
                left_swap = v
                break
        
        for j in range(hi - 1,i, -1):
            if l[j] < pivot:
                right_swap = j
                break

        # if all items from both swapped, partition success
        if left_swap == None and right_swap == None:
            break

        # now lomuto to finish remaining items
        elif left_swap == None:
            j = right - 1
            for k in reversed(range(left, right)):
                if l[k] > pivot:

                    l[k], l[j] = l[j], l[k]
                    yield (k, j)

                    j -= 1

            l[j], l[i] = l[i], l[j]
            yield(j, i)

            i = j
            break

        # lomuto for other side
        elif right_swap == None:
            j = left
            for k in range(left, right):
                if l[k] < pivot:

                    l[k], l[j] = l[j], l[k]
                    yield (k, j)

                    j += 1

            l[j], l[i] = l[i], l[j]
            yield(j, i)

            i = j
            break
        else:
            l[left_swap], l[right_swap] = l[right_swap], l[left_swap]
            yield(left_swap, right_swap)

            right, left = right_swap, left_swap + 1

    if i - lo > 1:
        yield from quicksort(l, lo, i)

    if hi - (i + 1) > 1:    
        yield from quicksort(l, i+1, hi)

if __name__ == "__main__":
    import random
    l = [random.randint(0, 2000) for _ in range(0, 1000)]
    s = sorted(l)
    print(l)
    for i in quicksort(l, 0, len(l)):
        print(i)
    print(l)
    print(l == s)
    