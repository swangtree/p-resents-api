"""
Utility calculation functions.

Calculate compatibility scores between givers and receivers.

NOTE: One team member will volunteer to implement this.
"""
from models.preferences import UserPreference


def calculate_utility(giver: UserPreference, receiver: UserPreference) -> float:
    """
    Calculate utility score from receiver's perspective.

    This function determines how happy the receiver would be if they received
    a gift from the giver, based on:
    - Giver's giving preferences (what kind of gifts they like to give)
    - Receiver's receiving preferences (what kind of gifts they like to receive)
    - Shared interests between giver and receiver
    - Custom weighting logic

    Args:
        giver: UserPreference object for the person giving the gift
        receiver: UserPreference object for the person receiving the gift

    Returns:
        float: Utility score (higher = better match)
               Suggested range: 0-10, but implementer has flexibility

    Example scoring approach:
        - Base score from matching gift preferences
        - Bonus for shared interests
        - Apply custom weights to different preference dimensions

    TODO: Team member to implement this function with their preferred weighting logic.
    """
    # PLACEHOLDER: Return a default score until implemented
    # Team member should replace this with actual utility calculation
    return 5.0


def calculate_shared_interests(giver: UserPreference, receiver: UserPreference) -> int:
    """
    Helper function to calculate number of shared interests.

    Args:
        giver: UserPreference object
        receiver: UserPreference object

    Returns:
        int: Number of shared interests
    """
    giver_interests = set(giver.preferred_interests)
    receiver_interests = set(receiver.preferred_interests)
    return len(giver_interests.intersection(receiver_interests))
