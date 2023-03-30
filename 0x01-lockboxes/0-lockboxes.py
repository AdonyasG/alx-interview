#!/usr/bin/env python3
"""
Module - lockboxes
"""


def canUnlockAll(boxes):
    """ DEfault """
    # Create a set to store the boxes that can be unlocked
    unlocked_boxes = {0}

    # Loop through the unlocked boxes and try to open new boxes
    while True:
        new_boxes = set()
        for box in unlocked_boxes.copy():
            for key in boxes[box]:
                if key not in unlocked_boxes and key < len(boxes):
                    # Add the new box to the set of unlocked boxes
                    new_boxes.add(key)
        if not new_boxes:
            break
        unlocked_boxes |= new_boxes

    # Check if all boxes can be unlocked
    return len(unlocked_boxes) == len(boxes)
