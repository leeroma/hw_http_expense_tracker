from random import choice


def random_colors(colors):
    colors_set = []
    while len(colors_set) != 3:
        color = choice(colors)
        if color not in colors_set:
            colors_set.append(color)

    return colors_set
