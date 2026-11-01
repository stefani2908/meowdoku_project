import validator as validator
from solver.backtracking import backtrack


def validate_all_puzzles(puzzles):

    results = []

    for puzzle_id, puzzle in puzzles.items():

        board_size = puzzle["board_size"]
        regions = puzzle["regions"]

        # Create an initial board
        solution = [
            [0 for _ in range(board_size)]
            for _ in range(board_size)
        ]

        # Add fixed cats
        for row, col in puzzle.get("fixed_cats", []):
            solution[row][col] = 1

        # Get region IDs
        region_ids = sorted({
            region_id
            for row in regions
            for region_id in row
        })

        # Run the solver
        stats = {
            "recursive_calls": 0,
            "backtracks": 0
        }

        result = backtrack(
            regions, region_ids, 0, solution, stats
        )

        if result is None:
            results.append({
                "Puzzle ID": puzzle_id,
                "Solution found": False,
                "All checks passed": False
            })
            continue

        # Validate the computed solution
        test_puzzle = puzzle.copy()
        test_puzzle["solution"] = result

        checks = [
            validator.validate_dimensions(test_puzzle),
            validator.validate_regions(test_puzzle),
            validator.validate_rows(test_puzzle),
            validator.validate_columns(test_puzzle),
            validator.validate_region_constraints(test_puzzle),
            validator.validate_diagonal_constraints(test_puzzle)
        ]

        results.append({
            "Puzzle ID": puzzle_id,
            "Solution found": True,
            "All checks passed": all(checks)
        })

    return results