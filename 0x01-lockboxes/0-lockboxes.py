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

        try:
            for key in boxes[box]:
                if key not in visited:
                    keys.add(key)
            visited.add(box)
        except IndexError:
            pass
    return len(visited) == len(boxes)
