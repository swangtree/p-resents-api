"""
Random Matching Algorithm

ASSIGNMENT: Person 1
Implements random gift exchange matching with expected statistics calculation.
"""
from typing import List, Dict
from models.preferences import UserPreference
from models.responses import RulesetStats, UserStats
import random


def calculate_statistics(preferences: List[UserPreference]) -> RulesetStats:
    """
    Calculate expected statistics for random matching.

    For a random perfect matching, each person has equal probability of being
    matched to any other person (excluding themselves and exclusions).

    Calculate expected mean and variance for EACH person, then compute overall stats.

    Args:
        preferences: List of user preference objects

    Returns:
        RulesetStats object with:
        - group_satisfaction_score: Average expected utility
        - group_fairness_score: Fairness metric (10 - std_dev, normalized)
        - min_utility: Theoretical minimum utility
        - max_utility: Theoretical maximum utility
        - std_dev: Standard deviation of expected utilities
        - user_stats: Per-user expected statistics

    TODO: Person 1 to implement
    Hint: For each receiver, calculate the average utility they would get
          from all possible givers (excluding themselves and exclusions)
    """
    # PLACEHOLDER IMPLEMENTATION
    user_stats = {}
    for pref in preferences:
        user_stats[pref.user_id] = UserStats(
            expected_utility=5.0,
            variance=2.0
        )

    return RulesetStats(
        group_satisfaction_score=5.0,
        group_fairness_score=7.0,
        min_utility=1.0,
        max_utility=10.0,
        std_dev=2.3,
        user_stats=user_stats
    )


def generate_matching(preferences: List[UserPreference], seed: int = None) -> Dict[str, str]:
    """
    Generate a random valid matching.

    Creates a random perfect matching (derangement) where:
    - No one gives to themselves
    - Exclusions are respected
    - Everyone gives to exactly one person
    - Everyone receives from exactly one person

    Args:
        preferences: List of user preference objects
        seed: Random seed for reproducibility (optional)

    Returns:
        Dict mapping giver_id -> receiver_id

    TODO: Person 1 to implement
    Hint: Generate random permutations until you find a valid derangement
    """
    # PLACEHOLDER IMPLEMENTATION
    if seed is not None:
        random.seed(seed)

    user_ids = [pref.user_id for pref in preferences]
    receivers = user_ids.copy()
    random.shuffle(receivers)

    # Simple placeholder - may produce invalid matching
    return dict(zip(user_ids, receivers))
