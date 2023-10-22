#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    function to check if all boxes can be unlocked
    """
    keys = set([0])
    updated = True

    while updated:
        old_keys = list(keys)
        old_length = len(old_keys)

        for item in old_keys:
            for new_key in boxes[item]:
                keys.add(new_key)

        if old_length == len(keys):
            updated = False

    if len(keys) >= len(boxes) - 1:
        return True
    else:
        return False
