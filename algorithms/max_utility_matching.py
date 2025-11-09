"""
Maximum Utility Matching Algorithm

ASSIGNMENT: Person 1
Implements maximum total utility matching using the Hungarian algorithm.
"""
from typing import List, Dict
from models.preferences import UserPreference
from models.responses import RulesetStats, UserStats
from utils.utility_calculator import calculate_utility


def calculate_statistics(preferences: List[UserPreference]) -> RulesetStats:
    """
    Calculate statistics for the maximum utility matching.

    Finds the matching that maximizes total group utility using the
    Hungarian algorithm (linear_sum_assignment from scipy).

    Args:
        preferences: List of user preference objects

    Returns:
        RulesetStats object with:
        - group_satisfaction_score: Average utility (total utility / num people)
        - group_fairness_score: Fairness metric based on variance
        - min_utility: Minimum utility in the optimal matching
        - max_utility: Maximum utility in the optimal matching
        - std_dev: Standard deviation of utilities in the matching
        - user_stats: Per-user utility in the optimal matching

    TODO: Person 1 to implement
    Steps:
    1. Create cost matrix using utility_calculator.calculate_utility()
    2. Use scipy.optimize.linear_sum_assignment(cost_matrix, maximize=True)
    3. Calculate statistics from the optimal matching
    4. Handle exclusions (set utility to -inf or very negative for excluded pairs)
    """
    # PLACEHOLDER IMPLEMENTATION
    user_stats = {}
    for pref in preferences:
        user_stats[pref.user_id] = UserStats(
            expected_utility=7.5,
            variance=0.0  # Single matching has no variance per person
        )

    return RulesetStats(
        group_satisfaction_score=7.5,
        group_fairness_score=6.5,
        min_utility=5.0,
        max_utility=10.0,
        std_dev=1.8,
        user_stats=user_stats
    )


def generate_matching(preferences: List[UserPreference]) -> Dict[str, str]:
    """
    Generate the optimal maximum utility matching.

    Uses the same algorithm as calculate_statistics to find the best matching.

    Args:
        preferences: List of user preference objects

    Returns:
        Dict mapping giver_id -> receiver_id

    TODO: Person 1 to implement
    Should use the same logic as calculate_statistics to ensure consistency.
    """
    # PLACEHOLDER IMPLEMENTATION
    matching, _ = _find_optimal_matching(preferences)
    return matching


def _find_optimal_matching(preferences: List[UserPreference]) -> tuple[Dict[str, str], RulesetStats]:
    """
    Internal helper to find optimal matching and stats.

    This can be shared between calculate_statistics and generate_matching
    to avoid code duplication.

    TODO: Person 1 to implement
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
