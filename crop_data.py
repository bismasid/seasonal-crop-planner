"""
crop_data.py

Stores seasonal crop data.

Includes each season and its respective fruits and vegetables.

Each crop's yield range is given in pounds (lbs). 
This is meant for a small plot of land. 
"""

CROP_DATA = {
    "spring": {
        "fruit": [
            {"name": "strawberries", "min_yield": 2, "max_yield": 6},
            {"name": "blueberries", "min_yield": 1, "max_yield": 4},
            {"name": "lemon", "min_yield": 1, "max_yield": 10},
            {"name": "raspberries", "min_yield": 1, "max_yield": 5},
        ],
        "vegetable": [
            {"name": "lettuce", "min_yield": 1, "max_yield": 3},
            {"name": "spinach", "min_yield": 1, "max_yield": 3},
            {"name": "peas", "min_yield": 1, "max_yield": 4},
            {"name": "radishes", "min_yield": 1, "max_yield": 3},
        ],
    },

    "summer": {
        "fruit": [
            {"name": "cherries", "min_yield": 5, "max_yield": 10},
            {"name": "watermelon", "min_yield": 10, "max_yield": 30},
            {"name": "cantaloupe", "min_yield": 5, "max_yield": 15},
            {"name": "peaches", "min_yield": 5, "max_yield": 20},
            {"name": "plum", "min_yield": 4, "max_yield": 16},
            {"name": "mango", "min_yield": 3, "max_yield": 27},
        ],
        "vegetable": [
            {"name": "zucchini", "min_yield": 5, "max_yield": 15},
            {"name": "cucumbers", "min_yield": 4, "max_yield": 12},
            {"name": "bell peppers", "min_yield": 3, "max_yield": 8},
            {"name": "green beans", "min_yield": 2, "max_yield": 8},
            {"name": "sweet corn", "min_yield": 4, "max_yield": 10},
        ],
    },

    "fall": {
        "fruit": [
            {"name": "apples", "min_yield": 10, "max_yield": 30},
            {"name": "pears", "min_yield": 8, "max_yield": 25},
            {"name": "cranberries", "min_yield": 2, "max_yield": 6},
            {"name": "pumpkin", "min_yield": 8, "max_yield": 40},
            {"name": "pomegranate", "min_yield": 8, "max_yield": 24},
            {"name": "grapes", "min_yield": 5, "max_yield": 20},
        ],
        "vegetable": [
            {"name": "kale", "min_yield": 2, "max_yield": 6},
            {"name": "carrots", "min_yield": 2, "max_yield": 8},
            {"name": "beets", "min_yield": 2, "max_yield": 6},
            {"name": "broccoli", "min_yield": 1, "max_yield": 4},
            {"name": "green beans", "min_yield": 3, "max_yield": 9},
        ],
    },

    "winter": {
        "fruit": [
            {"name": "oranges", "min_yield": 10, "max_yield": 30},
            {"name": "lemons", "min_yield": 5, "max_yield": 15},
            {"name": "persimmon", "min_yield": 5, "max_yield": 10},
            {"name": "grapefruit", "min_yield": 5, "max_yield": 20},
            {"name": "mandarins", "min_yield": 8, "max_yield": 25},
        ],
        "vegetable": [
            {"name": "cabbage", "min_yield": 2, "max_yield": 6},
            {"name": "brussels sprouts", "min_yield": 2, "max_yield": 5},
            {"name": "leeks", "min_yield": 2, "max_yield": 6},
            {"name": "potatoes", "min_yield": 7, "max_yield": 14},
        ],
    },
}
