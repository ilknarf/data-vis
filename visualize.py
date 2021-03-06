"""
Produce .png (potentially .svg) from pair swaps generated by the sorting
algorithms
"""

import cairo


def visualize(fun, l: list, width: int, height: int, name: str):
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)

    sorted_list = l.copy()
    swaps = [s for s in fun(sorted_list)]

    sctx = cairo.Context(surface)
    sctx.scale(width, height)
    sctx.rectangle(0, 0, 1, 1)
    sctx.set_source_rgb(1, 1, 1)
    sctx.fill()

    MAX_VALUE = sorted_list[-1]
    MIN_VALUE = sorted_list[0]
    LIST_LENGTH = len(l)
    SWAP_LENGTH = len(swaps)
    X_UNIT = width / (SWAP_LENGTH + 2)
    # print(X_UNIT)
    VIOLET = (0.7, 0, 0.9)
    BLUE = (0.7, 0.9, 1)
    Y_UNIT = height / (LIST_LENGTH * 1.05)
    # print(Y_UNIT)

    contexts = [None] * len(l)
    for i, val in enumerate(l):
        percent_max = (val - MIN_VALUE) / (MAX_VALUE - MIN_VALUE)
        color = [percent_max * c1 + (1 - percent_max) * c2
                 for c1, c2 in zip(VIOLET, BLUE)]

        ctx = cairo.Context(surface)
        ctx.set_source_rgb(*color)

        y_value = i * Y_UNIT

        ctx.translate(0, 0.05 * height)
        ctx.move_to(0, y_value)
        ctx.set_line_width(0.3 * Y_UNIT)
        ctx.line_to(X_UNIT, y_value)

        contexts[i] = ctx

    for i, swap in enumerate(swaps):
        x_value = (i + 2) * X_UNIT
        swap_0 = swap[0]
        swap_1 = swap[1]
        for j, ctx in enumerate(contexts):
            if swap_0 == j:
                ctx.line_to(x_value, swap_1 * Y_UNIT)

            elif swap_1 == j:
                ctx.line_to(x_value, swap_0 * Y_UNIT)

            else:
                ctx.line_to(x_value, j * Y_UNIT)

        contexts[swap_0], contexts[swap_1] = contexts[swap_1], contexts[swap_0]

    for i, ctx in enumerate(contexts):
        ctx.line_to(width, i * Y_UNIT)
        ctx.stroke()

    surface.write_to_png(f'{name}.png')


if __name__ == '__main__':
    from quicksort import quicksort
    from selection_sort import selection_sort
    from random import randint
    
    l = [randint(0, 50) for _ in range(0, 20)]

    visualize(quicksort, l, 512, 256, 'quicksort')
    visualize(selection_sort, l, 512, 256, 'selection')

