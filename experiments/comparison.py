import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics


def create_comparison(basic_results, mrv_results, puzzles):

    rows = []

    for puzzle_id in puzzles:

        basic = basic_results[puzzle_id]
        mrv = mrv_results[puzzle_id]

        rows.append({
            "Puzzle ID": puzzle_id,
            "Basic Calls": statistics.median(
                r["recursive_calls"] for r in basic
            ),
            "MRV Calls": statistics.median(
                r["recursive_calls"] for r in mrv
            ),
            "Basic Time": statistics.median(
                r["execution_time"] for r in basic
            ),
            "MRV Time": statistics.median(
                r["execution_time"] for r in mrv
            ),
            "Basic Backtracks": statistics.median(
                r["backtracks"] for r in basic
            ),
            "MRV Backtracks": statistics.median(
                r["backtracks"] for r in mrv
            )
        })

    return pd.DataFrame(rows)


def plot_comparison(comparison, basic_column, mrv_column,
                    title, ylabel, log_scale=False):

    x = np.arange(len(comparison))
    width = 0.35

    plt.figure(figsize=(10, 5))

    plt.bar(
        x - width / 2,
        comparison[basic_column],
        width,
        label="Basic Backtracking"
    )

    plt.bar(
        x + width / 2,
        comparison[mrv_column],
        width,
        label="MRV"
    )

    plt.title(title)
    plt.xlabel("Puzzle ID")
    plt.ylabel(ylabel)
    plt.xticks(x, comparison["Puzzle ID"])
    plt.legend()
    if log_scale:
        plt.yscale("log")
    plt.tight_layout()
    plt.show()