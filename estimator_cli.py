"""
Agile Story Point Estimator — CLI Version

Estimates Story Points based on three Agile criteria:
  - Complexity
  - Effort
  - Uncertainty

The combined score maps to Fibonacci story points.
"""

# Mapping from total score ranges to Fibonacci story point values
SCORE_TO_STORY_POINTS = [
    (range(3, 5),   1),
    (range(5, 7),   2),
    (range(7, 9),   3),
    (range(9, 11),  5),
    (range(11, 13), 8),
    (range(13, 15), 13),
    (range(15, 16), 21),
]

# Labels and descriptions for each rating level per criterion
CRITERION_LABELS = {
    "Complexity": {
        1: "Trivial change",
        2: "Simple change",
        3: "Moderate complexity",
        4: "Complex task",
        5: "Highly complex architecture change",
    },
    "Effort": {
        1: "Less than a few hours",
        2: "Up to one day",
        3: "Several days of work",
        4: "Large task",
        5: "Very large task",
    },
    "Uncertainty": {
        1: "Fully understood task",
        2: "Minor unknowns",
        3: "Some unknowns",
        4: "Significant unknowns",
        5: "Highly uncertain task",
    },
}


def map_score_to_story_points(score: int) -> int:
    """
    Convert a total score (3–15) into the corresponding Fibonacci story point value.

    Score ranges:
        3–4  -> 1 SP
        5–6  -> 2 SP
        7–8  -> 3 SP
        9–10 -> 5 SP
        11–12 -> 8 SP
        13–14 -> 13 SP
        15   -> 21 SP
    """
    for score_range, story_points in SCORE_TO_STORY_POINTS:
        if score in score_range:
            return story_points
    # Fallback — should never be reached with valid input
    raise ValueError(f"Score {score} is outside the valid range (3–15).")


def get_validated_input(criterion: str) -> int:
    """
    Prompt the user to enter a rating (1–5) for the given criterion.
    Displays descriptions for each level, then validates the input.
    Returns a valid integer between 1 and 5.
    """
    print(f"\n  {criterion}:")
    labels = CRITERION_LABELS[criterion]
    for value, description in labels.items():
        print(f"    {value} = {description}")

    while True:
        raw = input(f"  Enter {criterion} (1–5): ").strip()

        # Check that the input is a digit before converting
        if raw.isdigit():
            rating = int(raw)
            if 1 <= rating <= 5:
                return rating

        print("  Invalid input. Please enter a whole number between 1 and 5.")


def print_summary(complexity: int, effort: int, uncertainty: int) -> None:
    """
    Calculate the total score and story points, then print a formatted summary.
    """
    total_score = complexity + effort + uncertainty
    story_points = map_score_to_story_points(total_score)

    separator = "-" * 40

    print(f"\n{separator}")
    print("  Agile Story Point Estimation")
    print(separator)
    print(f"  Complexity:   {complexity}")
    print(f"  Effort:       {effort}")
    print(f"  Uncertainty:  {uncertainty}")
    print(separator)
    print(f"  Total Score:  {total_score}")
    print(f"\n  Estimated Story Points: {story_points} SP")
    print(separator)


def main() -> None:
    """
    Entry point for the CLI estimator.
    Greets the user, collects ratings for each criterion, and prints the result.
    """
    print("\n" + "=" * 40)
    print("  Agile Story Point Estimator")
    print("=" * 40)
    print(
        "\n  Story points are relative estimates used in Agile\n"
        "  to measure the effort and complexity of work.\n"
        "  Rate each factor from 1 (lowest) to 5 (highest)."
    )

    complexity  = get_validated_input("Complexity")
    effort      = get_validated_input("Effort")
    uncertainty = get_validated_input("Uncertainty")

    print_summary(complexity, effort, uncertainty)


if __name__ == "__main__":
    main()
