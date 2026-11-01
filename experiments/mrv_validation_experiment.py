from solver.mrv_backtracking import mrv_backtrack

from validator import (
    validate_dimensions,
    validate_regions,
    validate_rows,
    validate_columns,
    validate_region_constraints,
    validate_diagonal_constraints
)


def validate_all_puzzles_mrv(puzzles):

    results = []

    for puzzle_id, puzzle in puzzles.items():

        board_size = puzzle["board_size"]
        regions = puzzle["regions"]

        # Create an empty board
        solution = [
            [0 for _ in range(board_size)]
            for _ in range(board_size)
        ]

        # Add fixed cats, if present
        for row, col in puzzle.get("fixed_cats", []):
            solution[row][col] = 1

        # Get region IDs
        region_ids = sorted({
            region_id
            for row in regions
            for region_id in row
        })

        # Run MRV solver
        result = mrv_backtrack(
            regions,
            region_ids,
            solution
        )

        # Validate the result
        if result is not None:

            test_puzzle = {
                **puzzle,
                "solution": result
            }

            checks = [
                validate_dimensions(test_puzzle),
                validate_regions(test_puzzle),
                validate_rows(test_puzzle),
                validate_columns(test_puzzle),
                validate_region_constraints(test_puzzle),
                validate_diagonal_constraints(test_puzzle)
            ]

            all_checks_passed = all(checks)

        else:
            all_checks_passed = False

        results.append({
            "Puzzle ID": puzzle_id,
            "Solution found": result is not None,
            "All checks passed": all_checks_passed
        })

    return results