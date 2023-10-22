#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    function to check if all boxes can be unlocked
    """
    keys = set([0])
    visited = set()

    while keys:
        box = keys.pop()
        visited.add(box)

        try:
            for key in boxes[box]:
                if key not in visited:
                    keys.add(key)
        except IndexError:
            pass
    print(len(visited))
    print(len(boxes))

    return len(visited) - len(boxes) in [0, 1]
