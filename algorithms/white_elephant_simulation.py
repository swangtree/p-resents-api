"""
White Elephant Game Simulation

ASSIGNMENT: Person 3
Simulates 1000+ White Elephant games with stealing mechanics.
"""
from typing import List, Dict
from models.preferences import UserPreference
from models.responses import RulesetStats, UserStats
import random


def calculate_statistics(preferences: List[UserPreference], num_simulations: int = 1000) -> RulesetStats:
    """
    Run multiple White Elephant game simulations and return aggregate statistics.

    Game Mechanics:
    1. Each turn, player can either:
       - Open a new gift
       - Steal an already-opened gift from someone else
    2. Players choose gifts based on best utility fit
       - Suggested: Use practicality + novelty for gift selection
       - Implementer has flexibility to adjust this
    3. Happiness is calculated separately from decision-making:
       - Base utility from the gift they end up with
       - MINUS penalty from we_hate_being_stolen_from (if stolen from)
       - PLUS bonus from we_enjoy_stealing (if they stole)

    Args:
        preferences: List of user preference objects
        num_simulations: Number of game simulations to run (default 1000)

    Returns:
        RulesetStats object with:
        - group_satisfaction_score: Average satisfaction across all simulations
        - group_fairness_score: Fairness based on variance
        - std_dev: Standard deviation of utilities across simulations
        - avg_steals_per_game: Average number of steals per game
        - max_steals_observed: Maximum steals in any single game
        - simulations_run: Number of simulations actually run
        - user_stats: Per-user aggregate statistics

    TODO: Person 3 to implement
    Steps:
    1. Run num_simulations games with randomized play orders
    2. In each game:
       - Simulate player decisions (steal or open based on utility)
       - Track who stole and who was stolen from
       - Calculate final happiness including stealing modifiers
    3. Aggregate results across all simulations
    4. Return statistics

    Design decisions for implementer:
    - How to calculate gift utility (practicality + novelty suggested)
    - How much weight to give stealing modifiers
    - Stealing rules (max steals per item, etc.)
    """
    # PLACEHOLDER IMPLEMENTATION
    user_stats = {}
    for pref in preferences:
        user_stats[pref.user_id] = UserStats(
            avg_utility=6.0,
            utility_standard_deviation=1.5,
            times_stolen_from_pct=0.25,
            times_stole_pct=0.20
        )

    return RulesetStats(
        group_satisfaction_score=6.0,
        group_fairness_score=7.0,
        std_dev=1.8,
        avg_steals_per_game=8.5,
        max_steals_observed=15,
        simulations_run=num_simulations,
        user_stats=user_stats
    )


def generate_play_order(preferences: List[UserPreference], seed: int = None) -> List[str]:
    """
    Generate a randomized play order for the actual White Elephant game.

    This is used by /finalize_group to give the admin a random order
    for the actual game play.

    Args:
        preferences: List of user preference objects
        seed: Random seed for reproducibility (optional)

    Returns:
        List of user_ids in randomized play order

    TODO: Person 3 to implement
    Hint: Simply shuffle the user IDs randomly
    """
    # PLACEHOLDER IMPLEMENTATION
    if seed is not None:
        random.seed(seed)

    user_ids = [pref.user_id for pref in preferences]
    random.shuffle(user_ids)
    return user_ids


def _simulate_single_game(preferences: List[UserPreference]) -> Dict:
    """
    Internal helper to simulate a single White Elephant game.

    Returns game results including:
    - Final gift assignments
    - Who stole from whom
    - Number of steals
    - Individual happiness scores

    TODO: Person 3 to implement
    This is the core game simulation logic.
    """
    # PLACEHOLDER
    return {
        "assignments": {},
        "steals": 0,
        "happiness": {}
    }
