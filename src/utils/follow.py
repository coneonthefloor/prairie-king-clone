import pygame


def follow(target, follower, min_distance, max_distance, lerp=0.05):
    """Follow target.
    Returns a new position vector for the follower based off the target's
    position. The new position will be inside the min and max distance range.
    """
    target_vector = pygame.math.Vector2(*target)
    follower_vector = pygame.math.Vector2(*follower)
    new_follower_vector = pygame.math.Vector2(*follower)

    distance = follower_vector.distance_to(target_vector)
    if distance > min_distance:
        direction_vector = (target_vector - follower_vector) / distance
        min_step = max(0, distance - max_distance)
        max_step = distance - min_distance
        step = min_step + (max_step - min_step) * lerp
        new_follower_vector = follower_vector + direction_vector * step

    return new_follower_vector
