"""
crop_planner.py

Seasonal Crop Planner & Yield Predictor

This program asks the user what season is it and if they prefer to
plant fruits or vegetables. It then recommends realistic crops for that
season and category, displays expected yield in pounds (lbs) and shows the 
yield in a bar chart for easy understanding.

Created by Bisma Siddiqui
CIS 173 - Final Project
"""

import random
from typing import List, Dict
import matplotlib.pyplot as plt

from crop_data import CROP_DATA


def get_user_preferences() -> Dict[str, str]:
    # Asks user for the current season and desired crop category.

    print("🌱 Welcome to the Seasonal Crop Planner! 🌱")
    print("Let's figure out what you can plant.\n")

    # Ask for season
    valid_seasons = ["spring", "summer", "fall", "winter"]
    while True:
        season = input("What season is it? (spring/summer/fall/winter): ").strip().lower()
        if season in valid_seasons:
            break
        print("Please enter a valid season: spring, summer, fall, or winter.\n")

    # Ask for category
    valid_categories = ["fruit", "vegetable"]
    while True:
        category = input("Do you want to plant fruits or vegetables? ").strip().lower()
        if category in valid_categories:
            break
        elif category in ["fruits", "veggies", "vegetables"]:
            category = "fruit" if category.startswith("fruit") else "vegetable"
            break
        print("Please enter 'fruit' or 'vegetable'.\n")

    return {"season": season, "category": category}


def get_recommended_crops(season: str, category: str) -> List[Dict]:
    #Get the list of recommended crops for the given season and category.

    season_data = CROP_DATA.get(season, {})
    crops = season_data.get(category, [])
    return crops


def simulate_yield(crops: List[Dict], num_simulations: int = 20) -> Dict[str, float]:
    """
    Randomly samples the yield in pounds from min_yield and max_yield 
    multiple times and produces the average expected yield for each crop. 
    """
    results = {}

    for crop in crops:
        name = crop["name"]
        min_y = crop["min_yield"]
        max_y = crop["max_yield"]

        total_yield = 0
        for _ in range(num_simulations):
            simulated = random.randint(min_y, max_y)
            total_yield += simulated

        average_yield = total_yield / num_simulations
        results[name] = average_yield

    return results


def plot_yield_chart(yield_results: Dict[str, float], season: str, category: str) -> None:
    
    # Plot a bar chart of expected yields for each crop.

    if not yield_results:
        print("No yield results to plot.")
        return

    crop_names = list(yield_results.keys())
    yields = list(yield_results.values())

    plt.figure()
    plt.bar(crop_names, yields)
    plt.title(f"Expected Yields for {category.title()}s in {season.title()}")
    plt.xlabel("Crop")
    plt.ylabel("Expected Yield (lbs)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def print_recommendations(crops: List[Dict], season: str, category: str) -> None:
    
    # Print the list of crop recommendations.
    
    if not crops:
        print(f"\nSorry, there are no {category}s listed for {season} yet.")
        return

    print(f"\nIn {season.title()}, ideal {category}s you can plant include:\n")
    for crop in crops:
        name = crop["name"]
        min_y = crop["min_yield"]
        max_y = crop["max_yield"]
        print(f"  - {name} (typical yield: {min_y}–{max_y} lbs)")

    print("\nLet's see how many pounds you might harvest on average: ")


def main() -> None:
    """
    Main function to run the Seasonal Crop Planner program.
    """
    preferences = get_user_preferences()
    season = preferences["season"]
    category = preferences["category"]

    crops = get_recommended_crops(season, category)

    print_recommendations(crops, season, category)

    if not crops:
        return

    yield_results = simulate_yield(crops, num_simulations=20)

    print("\nExpected average yields (approximate):")
    for name, avg in yield_results.items():
        print(f"  - {name}: {avg:.1f} lbs")

    plot_yield_chart(yield_results, season, category)


if __name__ == "__main__":
    print("\n-----------------------------\n")
    main()
