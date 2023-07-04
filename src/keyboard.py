import pygame


_keys = {}


def is_key_down(key):
    if not key in _keys:
        _keys[key] = False
    return _keys[key]


def update_keys(events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            _keys[event.key] = True
        if event.type == pygame.KEYUP:
            _keys[event.key] = False
