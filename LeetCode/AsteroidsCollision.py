def asteroid_collision(asteroids):
    final_asteroids = []

    for asteroid in asteroids:
        while final_asteroids and asteroid < 0 < final_asteroids[-1]:
            if abs(asteroid) > abs(final_asteroids[-1]):
                final_asteroids.pop()
                continue
            elif abs(asteroid) == abs(final_asteroids[-1]):
                final_asteroids.pop()
            break
        else:
            final_asteroids.append(asteroid)

    return final_asteroids
