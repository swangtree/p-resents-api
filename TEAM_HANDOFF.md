# Team Handoff - P-resents API

## What's Been Completed ✅

### Controller Layer (Your Work)
- ✅ Complete FastAPI application structure
- ✅ Pydantic models for type safety and validation
- ✅ Route handlers for `/recalculate` and `/finalize_group`
- ✅ Service layer for orchestration
- ✅ Full test suite with 9 passing tests
- ✅ Interactive API documentation at `/docs`
- ✅ Error handling and validation
- ✅ CORS middleware configured
- ✅ Deployment ready (Dockerfile + fly.toml)

### What Team Needs to Implement

#### Person 1: Random Matching + Max Utility
**Files to edit:**
- `algorithms/random_matching.py`
- `algorithms/max_utility_matching.py`

**Functions to implement:**
1. `calculate_statistics()` - Calculate expected stats for the algorithm
2. `generate_matching()` - Generate actual pairings
3. Handle exclusions properly
4. Use `scipy.optimize.linear_sum_assignment()` for Max Utility

#### Person 2: Max Fairness
**Files to edit:**
- `algorithms/max_fairness_matching.py`

**Functions to implement:**
1. `calculate_statistics()` - Calculate stats for fair matching
2. `generate_matching()` - Generate fair pairings
3. Choose fairness definition (minimax recommended)

#### Person 3: White Elephant
**Files to edit:**
- `algorithms/white_elephant_simulation.py`

**Functions to implement:**
1. `calculate_statistics()` - Run 1000+ simulations
2. `generate_play_order()` - Random shuffle for play order
3. Implement game mechanics with stealing

#### Volunteer: Utility Calculator
**Files to edit:**
- `utils/utility_calculator.py`

**Functions to implement:**
1. `calculate_utility(giver, receiver)` - Calculate compatibility score
2. Combine giving/receiving preferences
3. Factor in shared interests
4. Apply custom weighting

## Testing Your Work

### 1. Start the API
```bash
uvicorn main:app --reload
```

### 2. Visit Interactive Docs
Open http://localhost:8000/docs in your browser

### 3. Try the Endpoints
Use the "Try it out" button in the docs, or use curl:

```bash
# Test /recalculate
curl -X POST "http://localhost:8000/recalculate" \
  -H "Content-Type: application/json" \
  -d '{
    "group_id": "test_001",
    "preferences": [
      {
        "user_id": "alice",
        "preference_practicality_giving": 4,
        "preference_practicality_receiving": 3,
        "preference_novelty_giving": 5,
        "preference_novelty_receiving": 2,
        "preference_thoughtfulness_giving": 3,
        "preference_thoughtfulness_receiving": 5,
        "preferred_interests": ["Coffee", "Tech"],
        "we_hate_being_stolen_from": 2,
        "we_enjoy_stealing": 4,
        "exclusions": []
      },
      {
        "user_id": "bob",
        "preference_practicality_giving": 2,
        "preference_practicality_receiving": 5,
        "preference_novelty_giving": 4,
        "preference_novelty_receiving": 3,
        "preference_thoughtfulness_giving": 5,
        "preference_thoughtfulness_receiving": 2,
        "preferred_interests": ["Hiking", "Coffee"],
        "we_hate_being_stolen_from": 4,
        "we_enjoy_stealing": 1,
        "exclusions": []
      }
    ]
  }'
```

### 4. Run Tests
```bash
pytest tests/ -v
```

## Current State

### API is Fully Functional
- ✅ All endpoints work with placeholder algorithm implementations
- ✅ Request/response validation working
- ✅ Error handling in place
- ✅ Tests all passing

### What Changes When You Implement Algorithms
When you replace the placeholder implementations in the algorithm files:
1. Statistics will be real (currently returns placeholder values)
2. Matchings will be optimal (currently returns simple round-robin)
3. Results will vary based on preferences (currently static)

### You Don't Need to Change
- ❌ Controller files (`controllers/*.py`)
- ❌ Service file (`services/matching_service.py`)
- ❌ Pydantic models (`models/*.py`)
- ❌ `main.py`

Just focus on implementing the algorithm functions!

## Tips

### Use the Existing Secret Santa Code
You have working implementations in `secret_santa_solution.py`:
- Can reference the logic
- May need to adapt to use `UserPreference` objects instead of dicts
- Need to call `calculate_utility()` instead of direct preference lookups

### Testing Your Algorithm
```python
# In your algorithm file, add a test at the bottom:
if __name__ == "__main__":
    from models.preferences import UserPreference

    # Create test preferences
    test_prefs = [
        UserPreference(
            user_id="alice",
            preference_practicality_giving=4,
            # ... other fields
        ),
        # ... more users
    ]

    # Test your function
    result = calculate_statistics(test_prefs)
    print(result)
```

Then run:
```bash
python algorithms/your_file.py
```

### Common Issues
1. **Import errors**: Make sure you're importing from the right modules
   ```python
   from models.preferences import UserPreference
   from utils.utility_calculator import calculate_utility
   ```

2. **Exclusions**: Don't forget to check `receiver.exclusions` list
   ```python
   if giver.user_id in receiver.exclusions:
       # Skip this pairing
   ```

3. **Return types**: Make sure to return the right Pydantic models
   ```python
   from models.responses import RulesetStats, UserStats
   ```

## Questions?
- Check `API_DESIGN.md` for full specification
- Check `README.md` for setup instructions
- Look at the tests in `tests/test_data.py` for examples
- Use `/docs` endpoint to see expected request/response formats

## Ready to Deploy
Once algorithms are implemented:
```bash
fly deploy
```

The API is already configured for Fly.io deployment!
