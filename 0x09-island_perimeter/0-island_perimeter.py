#!/usr/bin/python3
"""
Module 0-island_perimeter
"""


def island_perimeter(grid):
    """calculates perimeter of grid"""
    # Set the count of 1 and neighbours as 0.
    neigh = 0
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):

            if grid[row][col] != 1:
                continue

            # If 1 is found increase the count by 1.
            count += 1

            # Count the neighbours towards right and bottom.
            if (row < len(grid) - 1) and (grid[row + 1][col] == 1):
                neigh += 1

            if (col < len(grid[row]) - 1) and (grid[row][col + 1] == 1):
                neigh += 1

    # Each 1 will add 4 and each neighbour will subtract 2 from the perimeter.
    ans = 4 * count
    ans -= 2 * neigh

    # Return the ans.
    return ans
