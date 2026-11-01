from solver.backtracking import (
    get_region_cells,
    is_valid_placement
)


def get_legal_candidates(regions, region_id, solution):
    """
    Return all legal candidate cells for a region.
    """

    candidates = []

    region_cells = get_region_cells(regions, region_id)

    for row, col in region_cells:

        if is_valid_placement(solution, row, col):
            candidates.append((row, col))

    return candidates

def select_mrv_region(regions, region_ids, solution):
    """
    Select the unassigned region with the fewest legal candidates.
    """

    best_region = None
    best_candidates = None

    for region_id in region_ids:

        region_cells = get_region_cells(regions, region_id)

        # Skip regions that already contain a cat
        if any(solution[row][col] == 1 for row, col in region_cells):
            continue

        candidates = get_legal_candidates(
            regions,
            region_id,
            solution
        )

        # Select the region with the fewest candidates
        if best_candidates is None or len(candidates) < len(best_candidates):
            best_region = region_id
            best_candidates = candidates

    return best_region, best_candidates

def mrv_backtrack(regions, region_ids, solution, stats=None):
    """
    Solve a Meowdoku puzzle using MRV backtracking.
    """

    if stats is None:
        stats = {
            "recursive_calls": 0,
            "backtracks": 0
        }

    stats["recursive_calls"] += 1

    # Select the most constrained unassigned region
    region_id, candidates = select_mrv_region(
        regions,
        region_ids,
        solution
    )

    # All regions have been assigned
    if region_id is None:
        return solution

    # No legal candidates: backtrack
    if not candidates:
        return None

    # Try each candidate cell
    for row, col in candidates:

        solution[row][col] = 1

        result = mrv_backtrack(
            regions,
            region_ids,
            solution,
            stats
        )

        if result is not None:
            return result

        # Undo the placement
        solution[row][col] = 0
        stats["backtracks"] += 1

    return None