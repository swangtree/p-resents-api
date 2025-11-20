"""
Maximum Fairness Matching Algorithm

ASSIGNMENT: Person 2
Implements fairness-optimized matching (e.g., minimax or variance minimization).
"""
from typing import List, Dict
from models.preferences import UserPreference
from models.responses import RulesetStats, UserStats
from utils.utility_calculator import calculate_utility


def calculate_statistics(preferences: List[UserPreference]) -> RulesetStats:
    """
    Calculate statistics for the fairness-optimized matching.

    Finds a matching that optimizes for fairness. Possible approaches:
    - Minimax: Maximize the minimum utility (ensure no one gets a bad match)
    - Variance minimization: Minimize variance in utility scores
    - Egalitarian: Ensure everyone gets above a threshold

    Args:
        preferences: List of user preference objects

    Returns:
        RulesetStats object with:
        - group_satisfaction_score: Average utility in the fair matching
        - group_fairness_score: Fairness metric (should be high!)
        - min_utility: Minimum utility in the matching
        - max_utility: Maximum utility in the matching
        - std_dev: Standard deviation (should be low for fair matching)
        - user_stats: Per-user utility in the fair matching

    TODO: Person 2 to implement
    Design decisions:
    1. Choose your fairness metric (minimax recommended)
    2. Implement algorithm to optimize that metric
    3. Handle exclusions
    4. Calculate resulting statistics

    Hint for minimax: Try different matchings and pick the one with highest min utility.
          You can use random search, or implement a more sophisticated algorithm.
    """
    # PLACEHOLDER IMPLEMENTATION
    user_stats = {}
    for pref in preferences:
        user_stats[pref.user_id] = UserStats(
            expected_utility=6.5,
            variance=0.0
        )

    return RulesetStats(
        group_satisfaction_score=6.5,
        group_fairness_score=9.5,  # High fairness!
        min_utility=6.0,
        max_utility=7.5,
        std_dev=0.5,  # Low variance!
        user_stats=user_stats
    )


def generate_matching(preferences: List[UserPreference], seed: int = None) -> Dict[str, str]:
    """
    Generate a fairness-optimized matching.

    Uses the same algorithm as calculate_statistics to find the best matching.

    Args:
        preferences: List of user preference objects
        seed: Random seed if algorithm uses randomness

    Returns:
        Dict mapping giver_id -> receiver_id

    TODO: Person 2 to implement
    Should use the same logic as calculate_statistics to ensure consistency.
    """
    # PLACEHOLDER IMPLEMENTATION
    matching, _ = _find_fair_matching(preferences, seed)
    return matching


def _find_fair_matching(preferences: List[UserPreference], seed: int = None) -> tuple[Dict[str, str], RulesetStats]:
    """
    Internal helper to find fair matching and stats.

    This can be shared between calculate_statistics and generate_matching
    to avoid code duplication.

    TODO: Person 2 to implement
    """
    # PLACEHOLDER
    user_ids = [pref.user_id for pref in preferences]
    n = len(user_ids)

    # Simple placeholder matching
    matching = {}
    for i in range(n):
        giver = user_ids[i]
        receiver = user_ids[(i + 1) % n]
        matching[giver] = receiver

    stats = calculate_statistics(preferences)
    return matching, stats
