def get_region_cells(regions, region_id):
    """
    Return all coordinates belonging to a given region.

    Coordinates use Python's zero-based indexing.
    Cells are returned from top to bottom and left to right.
    """

    candidate_cells = []

    for i in range(len(regions)):
        for j in range(len(regions[i])):

            if regions[i][j] == region_id:
                candidate_cells.append((i, j))

    return candidate_cells

def is_valid_placement(solution, row, col):

    board_size = len(solution)

    # Check the row
    for j in range(board_size):
        if solution[row][j] == 1:
            return False

    # Check the column
    for i in range(board_size):
        if solution[i][col] == 1:
            return False

    # Check all four diagonal neighbours
    for row_offset in [-1, 1]:
        for col_offset in [-1, 1]:

            neighbour_row = row + row_offset
            neighbour_col = col + col_offset

            if 0 <= neighbour_row < board_size and 0 <= neighbour_col < board_size:
                if solution[neighbour_row][neighbour_col] == 1:
                    return False

    return True

def backtrack(regions, region_ids, region_index, solution, stats=None):
    """
    Recursively place one cat in each region.
    Returns a completed solution if one is found,
    otherwise returns None.
    """

    if stats is None:
        stats = {
            "recursive_calls": 0,
            "backtracks": 0
        }

    # Count every invocation of the recursive function
    stats["recursive_calls"] += 1

    # Base case: all regions have been processed
    if region_index == len(region_ids):
        return [row[:] for row in solution]

    # Select the current region
    current_region = region_ids[region_index]

    # Find its candidate cells
    candidate_cells = get_region_cells(regions, current_region)

    # Check whether this region already contains a fixed cat
    for row, col in candidate_cells:
        if solution[row][col] == 1:
            return backtrack(
                regions, region_ids, region_index + 1, solution, stats
            )

    # Try each candidate cell
    for row, col in candidate_cells:

        if is_valid_placement(solution, row, col):

            # Temporarily place a cat
            solution[row][col] = 1

            # Continue with the next region
            result = backtrack(
                regions, region_ids, region_index + 1, solution, stats
            )

            # Return if a complete solution was found
            if result is not None:
                return result

            # Otherwise, undo the tentative placement
            solution[row][col] = 0
            stats["backtracks"] += 1

    # No candidate worked in this region
    return None