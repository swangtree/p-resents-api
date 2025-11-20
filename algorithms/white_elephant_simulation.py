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


def simulate_single_game(preferences: List[UserPreference]) -> Dict:
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

    # note: novelty and practicality are scored on a range from 0-5 (?) 
    # initialize overall steal count of 0 
    # everyone: initilize my_turn to 1 
        # every time someone goes, -1 for my_turn 
        # every time someone gets stolen from +1 to my_turn
    # everyone: initilize happiness of 5 to begin with (the range will be 0-10) (number)
    # everyone: initialize hypothetical happiness of 5 to begin with (the range will be 0-10) (make it a list for easier comparison later?) 
    # make a dict with how many times a player steals and was stolen from? both numbers start at 0
    # make a dict with the gift that was the last stolen one (player: previous gift)
    # make a dict with the status of each gift? gift: novelty, practicality, opened/unopened, stolen/not stolen 
        # rule: gift can only be stolen [x] of times. could have the user choose, but i would say max 3 times. 
        # rule: gifts that are unopened cannot be stolen 
        # rule: you cannot immediately steal back the gift that was stolen from you 

    # happiness calculator: 
        # 1. find the distance between receiver's preferred novelty and giver's gift's novelty (gift_novelty - preferred_novelty)
        # 2. find the distance between receiver's preferred practicality and the giver's gift practicality (gift_practicality - preferred_practicality)
        # 3a. if the preferences and the gifts are exactly the same (the distances are 0), receiver's happiness = 9 (arbitrary number lmao. great, but leaves room for unexpected happiness) 
        # 3b. for every point above (gift > preferred), +1 to receiver's happiness. stop if receiver's happiness reaches 10 (max happiness) 
        # 3c. for every point below (gift < preferred), -1 from receiver's happiness. stop if receiver's happiness reaches 0 (no negative happiness) 


    # player #1 must open a gift (only option) 
        # 1. assign the giver's gift to player #1 in the dict 
        # 2. recalculate player #1 happiness using happiness calculator
        # 3. -1 to my_turn, making it 0
        
    # remaining players have the choice between opening or stealing, so for the current player: 
        # 1. recalculate hypothetical happiness: 
            # for every gift that is opened and steal =< 3 and was not the gift that was last stolen from the player (if that applies), use the happiness calculator 
                # only keep the highest hypothetical happiness as the final 
                # add bonus of we_enjoy_stealing to their highest hypothetical happiness 
            # if there are no gifts that meet that critera (open and steal =< 3), then automatically go to 2b (pick a new gift)
        # 2a. if hypothetical happiness > 5, steal from the player that has that gift  
            # assign the stolen gift to the current player in the dict 
            # recalculate the current player happiness by equating it to hypothetical happiness 
            # +1 to the overall steal count 
            # +1 to the current player's steal count, the player whose gift was stolen's stolen count, and the status of the gift's stolen count
            # update player: previous gift
            # player whose gift was stolen's happiness returns to 5
        # 2b. if hypothetical happiness < 5, pick a new gift 
            # assign the giver's gift to the current player in the dict 
            # recalculate the current player happiness using happiness calculator 
        # 3. -1 to my_turn, making it 0 

    # start from the beginning of the dict. the first person who has my_turn = 1, they get to go 
    # repeat steps 1-3 under "remaining players have the choice between opening or stealing..." until my_turn for everyone is 0 

    # recalculate happiness scores by now subtracting how much people disliked being stolen from 
        # if stolen > 0, then minus penalty from we_hate_being_stolen_from (the lowest happiness can go is 0)

    # return the final gift assignment 
    # return steal count and stolen count for each player 
    # return overall number of steals 
    # return the final and individual happiness score for each player

    # questions i have / things to think about: 
        # should perfect match = 9 or is there a "better" number? 
        # does the further the distance --> the more happy/unhappy people are? currently, i have +1/-1 for every step above/below, when it is probably not linear in reality? 
        # what happens if hypothetical happiness is the same across multiple gifts? choose one randomly? or what other way to tie break? 
        # i mix the we_enjoy_to_steal within the formula to decide whether to steal or not. i do not include it at the end if their end gift was not the gift that they stole. 
        # in contrast, i keep the we_hate_being_stolen_from until the end, because i don't think that influences someone's decision whether to steal or not. 
        # does that logic make sense? should i calculate we_enjoy_to_steal in the end happiness, even if they do not end up with the gift they stole? 

    # PLACEHOLDER
    return {
        "assignments": {},
        "steals": 0,
        "happiness": {}
    }
