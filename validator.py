#These functions will validate that the matrices are correct and the puzzles are possible to solve

def validate_dimensions(puzzle):

    regions = puzzle["regions"]
    solution = puzzle["solution"]
    board_size = puzzle["board_size"]

    if len(regions) != board_size:
        return False

    if len(solution) != board_size:
        return False

    for row in regions:
        if len(row) != board_size:
            return False

    for row in solution:
        if len(row) != board_size:
            return False

    # Update validation status
    puzzle["validation"]["dimensions_checked"] = True

    return True

def validate_regions(puzzle):

    regions = puzzle["regions"]
    board_size = puzzle["board_size"]

    # Find all unique region IDs
    region_ids = set()

    for row in regions:
        for region_id in row:
            region_ids.add(region_id)

    # Check that the number of regions equals board size
    if len(region_ids) != board_size:
        return False

    # Check connectivity of each region
    for region_id in region_ids:

        # Find all cells belonging to this region
        cells = set()

        for i in range(board_size):
            for j in range(board_size):
                if regions[i][j] == region_id:
                    cells.add((i, j))

        # Start flood-fill from the first cell
        start = next(iter(cells))
        visited = {start}
        stack = [start]

        while stack:
            i, j = stack.pop()

            # Check the four orthogonal neighbours
            neighbours = [
                (i - 1, j),
                (i + 1, j),
                (i, j - 1),
                (i, j + 1)
            ]

            for ni, nj in neighbours:

                if (ni, nj) in cells and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    stack.append((ni, nj))

        # If not all cells were reached, region is disconnected
        if visited != cells:
            return False

    # Update validation status
    puzzle["validation"]["regions_checked"] = True

    return True
def validate_rows(puzzle):

    solution = puzzle["solution"]
    board_size = puzzle["board_size"]

    # Check every row
    for row in solution:

        # Count the cats in the current row
        cat_count = sum(row)

        # Every row must contain exactly one cat
        if cat_count != 1:
            return False

    # Update validation status
    puzzle["validation"]["rows_checked"] = True

    return True

def validate_columns(puzzle):

    solution = puzzle["solution"]
    board_size = puzzle["board_size"]

    # Check every column
    for j in range(board_size):

        # Count the cats in the current column
        cat_count = 0

        for i in range(board_size):
            cat_count += solution[i][j]

        # Every column must contain exactly one cat
        if cat_count != 1:
            return False

    # Update validation status
    puzzle["validation"]["columns_checked"] = True

    return True
def validate_region_constraints(puzzle):

    regions = puzzle["regions"]
    solution = puzzle["solution"]
    board_size = puzzle["board_size"]

    # Find all unique region IDs
    region_ids = set()

    for row in regions:
        for region_id in row:
            region_ids.add(region_id)

    # Check the number of cats in every region
    for region_id in region_ids:

        cat_count = 0

        for i in range(board_size):
            for j in range(board_size):

                if regions[i][j] == region_id:
                    cat_count += solution[i][j]

        # Every region must contain exactly one cat
        if cat_count != 1:
            return False

    # Update validation status
    puzzle["validation"]["region_constraints_checked"] = True

    return True

def validate_diagonal_constraints(puzzle):

    solution = puzzle["solution"]
    board_size = puzzle["board_size"]

    # Check diagonal neighbours
    for i in range(board_size - 1):
        for j in range(board_size - 1):

            # Check diagonal down-right
            if solution[i][j] == 1 and solution[i + 1][j + 1] == 1:
                return False

            # Check diagonal down-left
            if j > 0 and solution[i][j] == 1 and solution[i + 1][j - 1] == 1:
                return False

    # Update validation status
    puzzle["validation"]["diagonal_constraints_checked"] = True

    return True