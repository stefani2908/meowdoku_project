#This file shows the meowdoku puzzles and their regions. Each color has a different number.
#This file also contains the solutions, where a 0 represents an empty field and 1 stands for the cat.
#The data is based from real app puzzles, which I have collected and transformed into matrices.

puzzle_165 = {
    "id": "165",
    "board_size": 10,
    "difficulty": None,
    "source": "Meowdoku",

    "regions": [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 2, 2, 3, 3, 3, 3, 4],
        [1, 1, 0, 0, 2, 5, 5, 5, 4, 4],
        [1, 1, 1, 0, 2, 2, 5, 5, 4, 4],
        [1, 1, 1, 0, 0, 2, 6, 5, 4, 0],
        [7, 7, 7, 7, 0, 2, 6, 6, 6, 0],
        [7, 7, 8, 8, 0, 6, 6, 6, 0, 0],
        [7, 9, 9, 8, 0, 6, 6, 0, 0, 0],
        [9, 9, 8, 8, 0, 0, 0, 0, 8, 0],
        [9, 9, 8, 8, 8, 8, 8, 8, 8, 0]
    ],

    "solution": [
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    ],

    "fixed_cats": [],

    "validation": {
        "dimensions_checked": False,
        "regions_checked": False,
        "rows_checked": False,
        "columns_checked": False,
        "region_constraints_checked": False,
        "diagonal_constraints_checked": False,
        "visual_comparison_completed": True
    }
}


puzzle_166 = {
    "id": "166",
    "board_size": 10,
    "difficulty": None,
    "source": "Meowdoku",

    "regions": [
        [0, 1, 1, 1, 2, 2, 2, 2, 2, 2],
        [0, 1, 1, 2, 2, 2, 2, 2, 2, 2],
        [0, 0, 0, 0, 0, 0, 3, 3, 4, 4],
        [0, 5, 5, 5, 3, 3, 3, 3, 3, 4],
        [0, 5, 5, 5, 5, 6, 6, 6, 6, 4],
        [0, 0, 0, 0, 0, 6, 6, 7, 7, 4],
        [0, 8, 8, 8, 0, 7, 7, 7, 4, 4],
        [0, 8, 9, 9, 0, 0, 7, 7, 4, 0],
        [0, 8, 9, 9, 0, 0, 7, 7, 4, 0],
        [0, 9, 9, 0, 0, 0, 0, 0, 0, 0]
    ],

    "solution": [
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    ],

    "fixed_cats": [],

    "validation": {
        "dimensions_checked": False,
        "regions_checked": False,
        "rows_checked": False,
        "columns_checked": False,
        "region_constraints_checked": False,
        "diagonal_constraints_checked": False,
        "visual_comparison_completed": True
    }

}

puzzle_170 = {
    "id": "170",
    "board_size": 10,
    "difficulty": "Hard",
    "source": "Meowdoku",

    "regions": [
        [0, 1, 1, 2, 2, 2, 3, 3, 3, 4],
        [0, 0, 1, 2, 9, 2, 5, 5, 5, 4],
        [1, 0, 1, 2, 9, 2, 6, 6, 5, 4],
        [1, 1, 1, 2, 9, 2, 2, 5, 5, 4],
        [1, 1, 2, 2, 9, 9, 9, 9, 5, 4],
        [1, 1, 1, 9, 9, 4, 4, 4, 4, 4],
        [7, 9, 9, 9, 7, 4, 7, 4, 7, 4],
        [7, 7, 7, 7, 7, 7, 7, 7, 7, 4],
        [7, 8, 7, 8, 8, 8, 7, 4, 7, 4],
        [8, 8, 8, 8, 7, 7, 7, 4, 4, 4]
    ],

    "solution": [
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    ],

    "fixed_cats": [],

    "validation": {
        "dimensions_checked": False,
        "regions_checked": False,
        "rows_checked": False,
        "columns_checked": False,
        "region_constraints_checked": False,
        "diagonal_constraints_checked": False,
        "visual_comparison_completed": True
    }
}

puzzle_174 = {
    "id": "174",
    "board_size": 9,
    "difficulty": None,
    "source": "Meowdoku",

    "regions": [
        [0, 0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 0, 2, 1, 1],
        [0, 0, 0, 0, 0, 0, 2, 1, 1],
        [0, 0, 3, 0, 0, 2, 2, 2, 1],
        [0, 0, 3, 0, 0, 4, 4, 4, 1],
        [5, 3, 3, 3, 0, 5, 4, 1, 1],
        [5, 6, 6, 6, 5, 5, 7, 8, 8],
        [5, 5, 6, 5, 5, 7, 7, 7, 8],
        [5, 5, 5, 5, 5, 5, 7, 8, 8]
    ],

    "solution": [
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1]
    ],

    "fixed_cats": [],

    "validation": {
        "dimensions_checked": False,
        "regions_checked": False,
        "rows_checked": False,
        "columns_checked": False,
        "region_constraints_checked": False,
        "diagonal_constraints_checked": False,
        "visual_comparison_completed": True
    }
}

puzzle_177 = {
    "id": "177",
    "board_size": 9,
    "difficulty": None,
    "source": "Meowdoku",

    "regions": [
        [0, 0, 0, 1, 2, 2, 2, 2, 2],
        [0, 1, 1, 1, 1, 1, 1, 2, 2],
        [0, 3, 3, 3, 1, 3, 1, 1, 2],
        [0, 0, 0, 3, 3, 3, 1, 2, 2],
        [4, 0, 5, 5, 5, 3, 2, 2, 2],
        [4, 0, 0, 5, 3, 3, 6, 2, 2],
        [4, 4, 4, 5, 5, 6, 6, 2, 2],
        [7, 4, 5, 5, 8, 2, 6, 6, 2],
        [7, 7, 8, 8, 8, 2, 2, 2, 2]
    ],

    "solution": [
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0]
    ],

    "fixed_cats": [],

    "validation": {
        "dimensions_checked": False,
        "regions_checked": False,
        "rows_checked": False,
        "columns_checked": False,
        "region_constraints_checked": False,
        "diagonal_constraints_checked": False,
        "visual_comparison_completed": True
    }
}

puzzle_178 = {
    "id": "178",
    "board_size": 10,
    "difficulty": None,
    "source": "Meowdoku",

    "regions": [
        [0, 1, 1, 1, 1, 1, 1, 1, 4, 4],
        [0, 1, 2, 2, 3, 3, 4, 4, 4, 4],
        [0, 0, 0, 2, 3, 3, 4, 5, 4, 0],
        [0, 6, 0, 2, 3, 3, 3, 5, 5, 0],
        [0, 6, 0, 2, 2, 2, 3, 5, 5, 0],
        [0, 6, 0, 0, 7, 7, 5, 5, 5, 0],
        [0, 6, 8, 0, 0, 7, 5, 5, 0, 0],
        [0, 8, 8, 8, 0, 7, 5, 5, 5, 0],
        [0, 8, 9, 9, 0, 7, 5, 5, 0, 0],
        [0, 9, 9, 9, 0, 0, 0, 0, 0, 0]
    ],

    "solution": [
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    ],

    "fixed_cats": [],

    "validation": {
        "dimensions_checked": False,
        "regions_checked": False,
        "rows_checked": False,
        "columns_checked": False,
        "region_constraints_checked": False,
        "diagonal_constraints_checked": False,
        "visual_comparison_completed": True
    }
}

puzzle_179 = {
    "id": "179",
    "board_size": 10,
    "difficulty": None,
    "source": "Meowdoku",

    "regions": [
        [0, 1, 1, 1, 2, 2, 2, 2, 2, 3],
        [1, 1, 1, 1, 2, 2, 2, 2, 2, 3],
        [1, 4, 1, 5, 2, 2, 2, 2, 6, 6],
        [4, 4, 4, 5, 2, 6, 6, 6, 6, 6],
        [4, 4, 5, 5, 5, 5, 5, 5, 6, 6],
        [4, 4, 4, 4, 5, 7, 6, 6, 6, 6],
        [4, 4, 8, 8, 7, 7, 7, 6, 6, 6],
        [4, 4, 4, 9, 9, 7, 7, 7, 6, 6],
        [9, 9, 9, 9, 9, 9, 7, 6, 6, 6],
        [9, 9, 7, 7, 7, 7, 7, 6, 6, 6]
    ],

    "solution": [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    ],

    "fixed_cats": [],

    "validation": {
        "dimensions_checked": False,
        "regions_checked": False,
        "rows_checked": False,
        "columns_checked": False,
        "region_constraints_checked": False,
        "diagonal_constraints_checked": False,
        "visual_comparison_completed": True
    }
}

puzzle_180 = {
    "id": "180",
    "board_size": 10,
    "difficulty": "Hard",
    "source": "Meowdoku",

    "regions": [
        [0, 1, 2, 2, 2, 2, 3, 3, 2, 2],
        [0, 1, 2, 4, 4, 2, 2, 2, 2, 2],
        [0, 0, 0, 0, 4, 4, 4, 4, 4, 2],
        [0, 4, 4, 4, 4, 5, 4, 4, 2, 2],
        [0, 5, 4, 5, 5, 5, 4, 2, 2, 2],
        [0, 5, 4, 4, 4, 5, 4, 4, 6, 2],
        [5, 5, 5, 4, 5, 5, 7, 6, 6, 2],
        [8, 8, 5, 5, 5, 5, 6, 6, 5, 5],
        [9, 8, 8, 8, 8, 5, 5, 5, 5, 5],
        [9, 9, 9, 9, 9, 9, 9, 9, 5, 5]
    ],

    "solution": [
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    ],

    "fixed_cats": [],

    "validation": {
        "dimensions_checked": False,
        "regions_checked": False,
        "rows_checked": False,
        "columns_checked": False,
        "region_constraints_checked": False,
        "diagonal_constraints_checked": False,
        "visual_comparison_completed": True
    }
}

puzzle_181 = {
    "id": "181",
    "board_size": 8,
    "difficulty": None,
    "source": "Meowdoku",
    "regions": [
    [0, 0, 0, 0, 2, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 3, 3],
    [4, 4, 1, 1, 5, 5, 3, 6],
    [4, 4, 4, 4, 5, 3, 3, 6],
    [4, 7, 7, 7, 5, 3, 6, 6],
    [4, 4, 7, 7, 5, 3, 5, 6],
    [4, 7, 7, 5, 5, 5, 5, 6],
    [7, 7, 5, 5, 6, 6, 6, 6]
],
    "solution": [
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]
],

    "fixed_cats": [1],

    "validation": {
        "dimensions_checked": False,
        "regions_checked": False,
        "rows_checked": False,
        "columns_checked": False,
        "region_constraints_checked": False,
        "diagonal_constraints_checked": False,
        "visual_comparison_completed": True
    }
}

puzzle_182 = {
    "id": "182",
    "board_size": 10,
    "difficulty": None,
    "source": "Meowdoku",

    "regions": [
        [0, 0, 0, 1, 1, 2, 2, 2, 2, 2],
        [0, 0, 0, 1, 1, 2, 0, 6, 2, 2],
        [3, 3, 0, 4, 1, 1, 0, 6, 6, 6],
        [3, 3, 0, 4, 4, 1, 0, 6, 8, 8],
        [3, 5, 0, 7, 7, 0, 0, 6, 8, 8],
        [3, 5, 0, 7, 7, 0, 9, 9, 8, 8],
        [3, 5, 0, 7, 7, 0, 9, 9, 8, 0],
        [5, 5, 0, 7, 7, 0, 9, 9, 8, 0],
        [5, 5, 0, 7, 0, 0, 0, 9, 9, 0],
        [5, 5, 0, 0, 0, 0, 0, 0, 0, 0]
    ],

    "solution": [
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    ],

    "fixed_cats": [],

    "validation": {
        "dimensions_checked": False,
        "regions_checked": False,
        "rows_checked": False,
        "columns_checked": False,
        "region_constraints_checked": False,
        "diagonal_constraints_checked": False,
        "visual_comparison_completed": True
    }
}