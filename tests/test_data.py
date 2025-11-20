"""
Test data for API testing.

Provides sample user preferences for testing endpoints and algorithms.
"""

# Sample preferences for 4 users
SAMPLE_PREFERENCES_4_USERS = [
    {
        "user_id": "alice_123",
        "preference_practicality_giving": 4,
        "preference_practicality_receiving": 3,
        "preference_novelty_giving": 5,
        "preference_novelty_receiving": 2,
        "preference_thoughtfulness_giving": 3,
        "preference_thoughtfulness_receiving": 5,
        "preferred_interests": ["Coffee", "Tech", "Books"],
        "we_hate_being_stolen_from": 2,
        "we_enjoy_stealing": 4,
        "exclusions": []
    },
    {
        "user_id": "bob_456",
        "preference_practicality_giving": 2,
        "preference_practicality_receiving": 5,
        "preference_novelty_giving": 4,
        "preference_novelty_receiving": 3,
        "preference_thoughtfulness_giving": 5,
        "preference_thoughtfulness_receiving": 2,
        "preferred_interests": ["Hiking", "Photography", "Coffee"],
        "we_hate_being_stolen_from": 4,
        "we_enjoy_stealing": 1,
        "exclusions": []
    },
    {
        "user_id": "charlie_789",
        "preference_practicality_giving": 3,
        "preference_practicality_receiving": 4,
        "preference_novelty_giving": 2,
        "preference_novelty_receiving": 5,
        "preference_thoughtfulness_giving": 4,
        "preference_thoughtfulness_receiving": 3,
        "preferred_interests": ["Gaming", "Tech", "Music"],
        "we_hate_being_stolen_from": 3,
        "we_enjoy_stealing": 3,
        "exclusions": ["bob_456"]  # Charlie excludes Bob
    },
    {
        "user_id": "diana_012",
        "preference_practicality_giving": 5,
        "preference_practicality_receiving": 2,
        "preference_novelty_giving": 1,
        "preference_novelty_receiving": 4,
        "preference_thoughtfulness_giving": 2,
        "preference_thoughtfulness_receiving": 5,
        "preferred_interests": ["Art", "Music", "Photography"],
        "we_hate_being_stolen_from": 5,
        "we_enjoy_stealing": 2,
        "exclusions": []
    }
]

# Sample recalculate request
SAMPLE_RECALCULATE_REQUEST = {
    "group_id": "test_group_001",
    "preferences": SAMPLE_PREFERENCES_4_USERS
}

# Sample finalize request for each ruleset
SAMPLE_FINALIZE_RANDOM = {
    "group_id": "test_group_001",
    "ruleset": "Random Matching",
    "preferences": SAMPLE_PREFERENCES_4_USERS,
    "seed": 42
}

SAMPLE_FINALIZE_MAX_UTILITY = {
    "group_id": "test_group_001",
    "ruleset": "Max Utility",
    "preferences": SAMPLE_PREFERENCES_4_USERS
}

SAMPLE_FINALIZE_MAX_FAIRNESS = {
    "group_id": "test_group_001",
    "ruleset": "Max Fairness",
    "preferences": SAMPLE_PREFERENCES_4_USERS,
    "seed": 42
}

SAMPLE_FINALIZE_WHITE_ELEPHANT = {
    "group_id": "test_group_001",
    "ruleset": "White Elephant",
    "preferences": SAMPLE_PREFERENCES_4_USERS,
    "seed": 42
}

# Edge case: minimum 2 users
SAMPLE_PREFERENCES_2_USERS = [
    SAMPLE_PREFERENCES_4_USERS[0],
    SAMPLE_PREFERENCES_4_USERS[1]
]

# Edge case: 1 user (should fail validation)
SAMPLE_PREFERENCES_1_USER = [
    SAMPLE_PREFERENCES_4_USERS[0]
]
