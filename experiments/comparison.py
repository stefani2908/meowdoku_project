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


def plot_overall_comparison(comparison):
    import matplotlib.pyplot as plt

    metrics = {
        "Recursive Calls": ("Basic Calls", "MRV Calls"),
        "Backtracks": ("Basic Backtracks", "MRV Backtracks")
    }

    totals = {
        name: (
            comparison[basic_column].sum(),
            comparison[mrv_column].sum()
        )
        for name, (basic_column, mrv_column) in metrics.items()
    }

    names = list(totals.keys())
    basic = [totals[name][0] for name in names]
    mrv = [totals[name][1] for name in names]

    x = range(len(names))
    width = 0.35

    fig, ax = plt.subplots(figsize=(9, 5))

    bars1 = ax.bar(
        [i - width / 2 for i in x],
        basic,
        width,
        label="Basic Backtracking"
    )

    bars2 = ax.bar(
        [i + width / 2 for i in x],
        mrv,
        width,
        label="MRV"
    )

    ax.set_yscale("log")
    ax.set_title("Overall Performance: Basic Backtracking vs MRV")
    ax.set_ylabel("Total Number (logarithmic scale)")
    ax.set_xticks(list(x))
    ax.set_xticklabels(names)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    for bars in (bars1, bars2):
        for bar in bars:
            height = bar.get_height()
            ax.annotate(
                f"{height:,.0f}",
                (bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),
                textcoords="offset points",
                ha="center"
            )

    plt.tight_layout()
    plt.show()
