import time
from solver.backtracking import backtrack


def benchmark_puzzle(puzzle, repetitions=5):

    results = []

    board_size = puzzle["board_size"]
    regions = puzzle["regions"]

    region_ids = sorted({
        region_id
        for row in regions
        for region_id in row
    })

    for run in range(repetitions):

        # Create a fresh board
        solution = [
            [0 for _ in range(board_size)]
            for _ in range(board_size)
        ]

        # Add fixed cats
        for row, col in puzzle.get("fixed_cats", []):
            solution[row][col] = 1

        # Initialise counters
        stats = {
            "recursive_calls": 0,
            "backtracks": 0
        }

        # Measure execution time
        start_time = time.perf_counter()

        result = backtrack(
            regions,
            region_ids,
            0,
            solution,
            stats
        )

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        if result is None:
            raise ValueError(
                f"Puzzle {puzzle['id']} could not be solved."
            )

        results.append({
            "execution_time": execution_time,
            "recursive_calls": stats["recursive_calls"],
            "backtracks": stats["backtracks"]
        })

    return results