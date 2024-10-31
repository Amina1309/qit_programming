import numpy as np


def if_asteroids_in_harmony(direct):
    # Check if the list is empty
    if len(direct) == 0:
        return True

    # Find the index of the first occurrence of 1
    try:
        first_one_index = np.where(direct == 1)[0][0]
    except ValueError:
        return np.all(direct == -1)

    # Check if all elements before the first 1 are -1
    for i in range(first_one_index.item()):
        if direct[i] != -1:
            return False

    # Check if all elements after the first 1 are 1
    for i in range(first_one_index, len(direct)):
        if direct[i] != 1:
            return False

    return True


def asteroids_collide(i, asteroids, new_directions):
    if new_directions[i] == 0:
        return new_directions
    else:
        for j in range(i + 1, len(asteroids)):
            if new_directions[j] == 0:
                continue
            else:
                if new_directions[j] < 0 < new_directions[i]:
                    if abs(asteroids[i]) > abs(asteroids[j]):
                        new_directions[j] = 0
                    elif abs(asteroids[i]) < abs(asteroids[j]):
                        new_directions[i] = 0
                    else:
                        new_directions[i] = 0
                        new_directions[j] = 0
                else:
                    break

    return new_directions


def asteroid_collision(asteroids):
    new_asteroids = asteroids
    new_directions = np.sign(asteroids)

    while not if_asteroids_in_harmony(new_directions[new_directions != 0]):
        for i in range(len(asteroids) - 1):
            new_directions = asteroids_collide(i, asteroids, new_directions)

    return [asteroids[i] for i in range(0, len(asteroids)) if new_directions[i] != 0]





