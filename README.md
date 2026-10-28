### Description
When calling `apply_category_discount(category, discount_percent)` on an `ExpenseTracker` instance, the expense amounts in the target category are overwritten with the discount value itself rather than having the discount subtracted from the original amount.

### Steps to Reproduce
1. Initialize `ExpenseTracker(1000.00)`
2. Add an expense: `add_expense("Groceries", 200.00, "Food")`
3. Apply a 10% discount: `apply_category_discount("Food", 10.0)`
4. Check category total with `get_expenses_by_category("Food")`

### Expected Behavior
A 10% discount on `$200.00` should reduce the amount by `$20.00`, resulting in a new total of `$180.00`. Running `python -m unittest test_tracker.py` should pass all 4 tests.

### Actual Behavior
The category total becomes `$20.00` (which is 10% of 200, effectively applying a 90% discount). Furthermore, applying a `0%` discount wipes out the expense to `$0.00`.

### Test Failure Output
```text
FAIL: test_apply_category_discount (test_tracker.TestExpenseTracker)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_tracker.py", line 22, in test_apply_category_discount
    self.assertEqual(self.tracker.get_expenses_by_category("Food"), 80.00)
AssertionError: 20.0 != 80.0